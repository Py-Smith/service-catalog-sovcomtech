from fastapi import APIRouter, Depends, Request

from services.service_system import (SystemServiceTeams,
                                     get_system_service_teams)

router = APIRouter()


# TODO: Добавить описание методов и пагинацию
@router.get('/{service_system_id}/main_teams', description='name1')
async def get_main_teams_by_id(service_system_id: int,
                               request: Request,
                               db: SystemServiceTeams = Depends(get_system_service_teams)):
    """Get information about all categories"""
    return await db.get_main_teams_by_id(request=request, service_system_id=service_system_id)


@router.get('/{service_system_id}/competence_teams', description='name1')
async def get_competence_teams_by_id(service_system_id: int,
                                     request: Request,
                                     db: SystemServiceTeams = Depends(get_system_service_teams)):
    """Get information about all categories"""
    return await db.get_competence_teams_by_id(request=request, service_system_id=service_system_id)
