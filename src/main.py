import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import Redis

from api.v1 import system
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

# TODO: Заменить на Guvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True, workers=2)
