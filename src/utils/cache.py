"""Упрощение работы с кешем"""
import orjson
from fastapi import Request
from pydantic import BaseModel

from core.config import settings
from db import redis


def get_data_from_cache(func):
    async def inner(*args, **kwarg):

        request: Request = kwarg.get('request')
        cache_key_name: str = get_chache_name(request)
        cache_data = await redis.redis.get(cache_key_name)

        if cache_data:
            return orjson.loads(cache_data)

        result = await func(*args, **kwarg)
        # TODO: Убрать когда все данные будут возвращаться в моделях pydantic
        if isinstance(result, BaseModel):
            result = result.model_dump()

        await redis.redis.set(name=cache_key_name, value=orjson.dumps(result), ex=settings.redis_ex)
        return result
    return inner


def get_chache_name(request: Request) -> str:
    if request.url.query:
        return f'{request.url.path}/{request.url.query}'
    return request.url.path
