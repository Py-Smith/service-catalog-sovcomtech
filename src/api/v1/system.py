from fastapi import APIRouter, Depends, Request

from core.descriptions import SystemApiDescription
from services.system import SystemInfoService, get_systems

router = APIRouter()


@router.get('/', description=SystemApiDescription.all_system_api)
async def get_systems_service(request: Request,
                              db: SystemInfoService = Depends(get_systems)):
    """Get information about all system"""
    return await db.get_all_systems(request=request)


@router.get('/{system_id}', description=SystemApiDescription.system_by_api)
async def get_system_info(request: Request,
                          system_id: int,
                          db: SystemInfoService = Depends(get_systems)):
    """Get information about system by id"""
    return await db.get_system_info(request=request, system_id=system_id)


@router.get('/{system_id}/service', description=SystemApiDescription.system_service_api)
async def get_system_info_service(request: Request,
                                  system_id: int,
                                  db: SystemInfoService = Depends(get_systems)):
    """Get information service for system"""
    return await db.get_system_service_info(request=request, system_id=system_id)
