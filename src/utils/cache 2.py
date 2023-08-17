"""Упрощение работы с кешем"""

import orjson

from core.config import settings
from db import redis


def get_data_from_cache(func):
    async def inner(*args, **kwarg):
        request = kwarg.get('request')
        cache_data = await redis.redis.get(request.url.path)

        if cache_data:
            return orjson.loads(cache_data)

        result = await func(*args, **kwarg)
        await redis.redis.set(name=request.url.path, value=orjson.dumps(result), ex=settings.redis_ex)
        return result
    return inner
