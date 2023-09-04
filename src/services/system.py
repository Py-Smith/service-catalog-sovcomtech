from functools import lru_cache

from aioredis import Redis
from fastapi import Depends, Request
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from db.redis import get_redis
from models.database.schema import (MethodProvidingService, PyrusUsers,
                                    Service, System, SystemService, Timetable)
from models.response.system import (PaginateSystemModel, SystemErrorModel,
                                    SystemModel, SystemServiceListModel,
                                    SystemServiceModel)
from utils.cache import get_data_from_cache


class SystemInfoService:
    """Class service for get information about systems"""
    def __init__(self, session: AsyncSession, redis: Redis):
        self.session = session
        self.redis = redis

    @get_data_from_cache
    async def get_all_systems(self, *, request: Request,
                              page: int, limit: int) -> PaginateSystemModel:
        """Get information about all systems"""

        select_expression = select(System.id,
                                   System.name,
                                   System.description
                                   ).select_from(System).offset(page * limit).limit(limit)

        query = await self.session.execute(select_expression)
        result: list = [SystemModel(**dict(c)) for c in query.mappings().all()]
        model = PaginateSystemModel(result=result, page=page, limit=limit, count=len(result))
        return model

    @get_data_from_cache
    async def get_system_info(self, *, request: Request, system_id: int) -> SystemModel | SystemErrorModel:
        """Get information about system by id"""
        query = await self.session.execute(
            select(System.id,
                   System.name,
                   System.description
                   )
            .select_from(System)
            .where(System.id == system_id))

        result: SystemModel = dict(query.mappings().first())  # type: ignore
        return SystemModel(**result)

    @get_data_from_cache
    async def get_system_service_info(self, *, request: Request, system_id: int) -> list[SystemServiceModel]:
        """Get information about system by id"""

        query = await self.session.execute(
            select(SystemService.id.label('id'),
                   System.name.label('system_name'),
                   func.json_build_object('id', Service.id,
                                          'name', Service.name,
                                          'description', Service.description,
                                          'time_to_request', SystemService.plan_time,
                                          'start_support_time', SystemService.start_support_time,
                                          'end_support_time', SystemService.end_support_time,
                                          'method_providing', MethodProvidingService.name).label('service'),
                   func.json_build_object('id', PyrusUsers.id,
                                          'name', PyrusUsers.username,
                                          'pyrus_id', PyrusUsers.pyrus_id,
                                          'email', PyrusUsers.email,
                                          'department', PyrusUsers.department,
                                          'management', PyrusUsers.management,
                                          'divizion', PyrusUsers.divizion).label('owner'),
                   func.json_build_object('id', Timetable.id,
                                          'name', Timetable.name,
                                          'description', Timetable.description).label('calendar'))
            .select_from(SystemService)
            .join(System, SystemService.system_id == System.id)
            .join(Service, SystemService.service_id == Service.id)
            .join(PyrusUsers, SystemService.supervizor_id == PyrusUsers.id)
            .join(Timetable, SystemService.timetable_id == Timetable.id)
            .join(MethodProvidingService, SystemService.method_providing_service_id == MethodProvidingService.id)
            .where(SystemService.system_id == system_id))

        result: list = [SystemServiceModel(**dict(c)) for c in query.mappings().all()]  # type: ignore
        return SystemServiceListModel(result=result)


@lru_cache()
def get_systems(
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis)
) -> SystemInfoService:
    return SystemInfoService(session, redis)
