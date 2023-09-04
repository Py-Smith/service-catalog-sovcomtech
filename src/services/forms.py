from functools import lru_cache

from aioredis import Redis
from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from db.redis import get_redis
from models.database.schema import PyrusForms, SystemServiceForms
from models.response.forms import FormModel, FromsListModel
from utils.cache import get_data_from_cache


class FormsService:
    """Class service for get information about systems"""
    def __init__(self, session: AsyncSession, redis: Redis):
        self.session = session
        self.redis = redis

    # TODO: подумать как убрать паараметр request: Request из функции
    @get_data_from_cache
    async def get_forms_by_system_service_id(self, *, request: Request, system_service_id: int) -> list:
        """Get information about form by system service id"""
        query = await self.session.execute(
            select(PyrusForms.id,
                   PyrusForms.form_id,
                   PyrusForms.form_name
                   )
            .select_from(SystemServiceForms)
            .join(PyrusForms, SystemServiceForms.pyrusforms_id == PyrusForms.id)
            .where(SystemServiceForms.systemservice_id == system_service_id))

        result: list = [FormModel(**dict(c)) for c in query.mappings().all()]
        return FromsListModel(result=result)

    # TODO: подумать как убрать паараметр request: Request из функции
    @get_data_from_cache
    async def get_forms_by_id(self, *, request: Request, form_id: int) -> list:
        """Get information about form by id"""
        query = await self.session.execute(
            select(PyrusForms.id,
                   PyrusForms.form_id,
                   PyrusForms.form_name)
            .select_from(PyrusForms)
            .where(PyrusForms.id == form_id))

        result: FormModel = dict(query.mappings().first())  # type: ignore
        return FormModel(**result)


@lru_cache()
def get_forms(
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis)
) -> FormsService:
    return FormsService(session, redis)
