import aioredis
from fastapi import Depends, FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn
from db.postgres import get_session, engine

from api.v1 import system
from core.config import settings

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


app.include_router(system.router, prefix='/api/v1/system', tags=['system'])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True, workers=2)