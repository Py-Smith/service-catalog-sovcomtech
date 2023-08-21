from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import Redis

from api.v1 import category, service_system, system
from core.config import settings
from db import redis

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port, decode_responses=True)


@app.on_event('shutdown')
async def shutdown():
    await redis.redis.close()


app.include_router(system.router, prefix='/api/v1/system', tags=['system'])
app.include_router(category.router, prefix='/api/v1/category', tags=['category'])
app.include_router(service_system.router, prefix='/api/v1/service_system', tags=['service_system'])
