import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import Redis
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import category, forms, system, teams
from core.config import settings
from db import elastic, redis
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event('startup')
async def startup():
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port, decode_responses=True)
    elastic.es = AsyncElasticsearch(hosts=[f'{settings.es_http_protocol}://{settings.es_host}:{settings.es_port}'])


@app.on_event('shutdown')
async def shutdown():
    await redis.redis.close()
    await redis.redis.wait_closed()
    await elastic.es.close()


app.include_router(system.router, prefix='/api/v1/system', tags=['system'])
app.include_router(category.router, prefix='/api/v1/category', tags=['category'])
app.include_router(teams.router, prefix='/api/v1/teams', tags=['teams'])
app.include_router(forms.router, prefix='/api/v1/forms', tags=['forms'])
# FIXME: Убрать на проде. Переключить на гуникорн
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True, workers=2)
