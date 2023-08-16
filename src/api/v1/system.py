from fastapi import APIRouter, Depends, Request

from services.system import SystemInfoService, get_systems

router = APIRouter()


@router.get('/', description='test')
async def get_systems_service(request: Request,
                              db: SystemInfoService = Depends(get_systems)):

    return await db.get_all_systems(request=request)


@router.get('/{system_id}', description='test2')
async def get_system_info_service(request: Request,
                                  system_id: int,
                                  db: SystemInfoService = Depends(get_systems)):
    return await db.get_system_info(request=request, system_id=system_id)
