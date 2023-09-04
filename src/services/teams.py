from functools import lru_cache

from aioredis import Redis
from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.postgres import get_session
from db.redis import get_redis
from models.database.schema import (CompetenceTeams, MainTeams,
                                    SystemServiceCompetenceTeams,
                                    SystemServiceMainTeams)
from models.response.teams import (CompetenceTeamsListModel,
                                   CompetenceTeamsModel, MainTeamsListModel,
                                   MainTeamsModel)
from utils.cache import get_data_from_cache


class TeamsService:
    """Class service for get information about systems"""
    def __init__(self, session: AsyncSession, redis: Redis):
        self.session = session
        self.redis = redis

    # TODO: подумать как убрать паараметр request: Request из функции
    @get_data_from_cache
    async def get_main_teams_by_id(self, *, request: Request, service_system_id: int) -> list:
        """Get information about system by id"""
        query = await self.session.execute(
            select(MainTeams.id,
                   MainTeams.role_id,
                   MainTeams.role_name,
                   MainTeams.plan_time,
                   MainTeams.pyrus_stage,
                   MainTeams.start_support_time,
                   MainTeams.end_support_time
                   )
            .select_from(SystemServiceMainTeams)
            .join(MainTeams, SystemServiceMainTeams.systemservicemainteams_id == MainTeams.id)
            .where(SystemServiceMainTeams.systemservice_id == service_system_id))

        result: list = [MainTeamsModel(**dict(c)) for c in query.mappings().all()]
        return MainTeamsListModel(result=result)

    # TODO: подумать как убрать паараметр request: Request из функции
    @get_data_from_cache
    async def get_competence_teams_by_id(self, *, request: Request, service_system_id: int) -> list:
        """Get information about system by id"""
        query = await self.session.execute(
            select(CompetenceTeams.id,
                   CompetenceTeams.role_id,
                   CompetenceTeams.role_name,
                   CompetenceTeams.plan_time,
                   CompetenceTeams.pyrus_stage,
                   CompetenceTeams.start_support_time,
                   CompetenceTeams.end_support_time
                   )
            .select_from(SystemServiceCompetenceTeams)
            .join(CompetenceTeams, SystemServiceCompetenceTeams.systemserviceсompetenceteams_id == CompetenceTeams.id)
            .where(SystemServiceCompetenceTeams.systemservice_id == service_system_id))

        result: list = [CompetenceTeamsModel(**dict(c)) for c in query.mappings().all()]
        return CompetenceTeamsListModel(result=result)


@lru_cache()
def get_system_service_teams(
        session: AsyncSession = Depends(get_session),
        redis: Redis = Depends(get_redis)
) -> TeamsService:
    return TeamsService(session, redis)
