from functools import lru_cache

from aioredis import Redis
from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from db.redis import get_redis
from models.database.system import SystemCategory
from utils.cache import get_data_from_cache


class SystemCategoryInfoService:
    """Class service for get information about systems"""
    def __init__(self, session: AsyncSession, redis: Redis):
        self.session = session
        self.redis = redis

    @get_data_from_cache
    async def get_all_categories(self, request: Request) -> list:
        """Get information about all systems"""
        query = await self.session.execute(
            select(SystemCategory.id,
                   SystemCategory.name,
                   SystemCategory.description
                   )
            .select_from(SystemCategory))
        result: list = [dict(c) for c in query.mappings().all()]
        return result

    # TODO: подумать как убрать паараметр request: Request из функции
    @get_data_from_cache
    async def get_category_info_by_id(self, request: Request, category_id: int) -> dict:
        """Get information about system by id"""
        query = await self.session.execute(
            select(SystemCategory.id,
                   SystemCategory.name,
                   SystemCategory.description
                   )
            .select_from(SystemCategory)
            .where(SystemCategory.id == category_id))

        try:
            result: dict = dict(query.mappings().first())  # type: ignore
            return result
        except TypeError:
            return {}


@lru_cache()
def get_categories(
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis)
) -> SystemCategoryInfoService:
    return SystemCategoryInfoService(session, redis)
