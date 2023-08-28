from fastapi import APIRouter, Depends, Request

from core.descriptions import SystemServiceDescription
from services.service_system import (SystemServiceTeams,
                                     get_system_service_teams)

router = APIRouter()


# TODO: Добавить описание методов и пагинацию
@router.get('/{service_system_id}/main_teams', description=SystemServiceDescription.main_teams_api)
async def get_main_teams_by_id(service_system_id: int,
                               request: Request,
                               db: SystemServiceTeams = Depends(get_system_service_teams)):
    """Get information about main teams in service"""
    return await db.get_main_teams_by_id(request=request, service_system_id=service_system_id)


@router.get('/{service_system_id}/competence_teams', description=SystemServiceDescription.competence_teams_api)
async def get_competence_teams_by_id(service_system_id: int,
                                     request: Request,
                                     db: SystemServiceTeams = Depends(get_system_service_teams)):
    """Get information about competence teams in service"""
    return await db.get_competence_teams_by_id(request=request, service_system_id=service_system_id)
