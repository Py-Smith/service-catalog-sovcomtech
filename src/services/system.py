from functools import lru_cache

import orjson
from aioredis import Redis
from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db.postgres import get_session
from db.redis import get_redis
from models.database.system import System


class SystemInfoService:
    """Class service for get information about systems"""
    def __init__(self, session: AsyncSession, redis: Redis):
        self.session = session
        self.redis = redis

    async def get_all_systems(self, request: Request) -> list:
        """Get information about all systems"""

        cache_data = await self.redis.get(request.url.path)
        if cache_data:
            return orjson.loads(cache_data)

        query = await self.session.execute(
            select(System.id,
                   System.name,
                   System.description,
                   System.category_id
                   )
            .select_from(System))
        result: list = [dict(c) for c in query.mappings().all()]
        await self.redis.set(name=request.url.path, value=orjson.dumps(result), ex=settings.redis_ex)

        return result

    async def get_system_info(self, request: Request, system_id: int) -> dict:
        """Get information about system by id"""

        cache_data = await self.redis.get(request.url.path)
        if cache_data:
            return orjson.loads(cache_data)

        query = await self.session.execute(
            select(System.id,
                   System.name,
                   System.description
                   )
            .select_from(System)
            .where(System.id == system_id))

        try:
            result: dict = dict(query.mappings().first())  # type: ignore
            await self.redis.set(name=request.url.path, value=orjson.dumps(result), ex=settings.redis_ex)
            return result
        except TypeError:
            return {}


@lru_cache()
def get_systems(
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis)
) -> SystemInfoService:
    return SystemInfoService(session, redis)
