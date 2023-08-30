from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from core.descriptions import PagingDescription, SystemApiDescription
from models.response.system import (PaginateSystemModel, SystemErrorModel,
                                    SystemModel, SystemServiceListModel)
from services.system import SystemInfoService, get_systems

router = APIRouter()


@router.get('/',
            response_model=PaginateSystemModel,
            description=SystemApiDescription.all_system_api
            )
async def get_all_systems(request: Request,
                          page: Annotated[int, Query(description=PagingDescription.page)] = 0,
                          limit: Annotated[int, Query(description=PagingDescription.limit)] = 50,
                          db: SystemInfoService = Depends(get_systems)):
    """Get information about all system"""
    return await db.get_all_systems(request=request, page=page, limit=limit)


@router.get('/{system_id}',
            response_model=SystemModel | SystemErrorModel,
            description=SystemApiDescription.system_by_api
            )
async def get_system_info(request: Request,
                          system_id: int,
                          db: SystemInfoService = Depends(get_systems)):
    """Get information about system by id"""
    try:
        return await db.get_system_info(request=request, system_id=system_id)
    except TypeError:
        return SystemErrorModel


@router.get('/{system_id}/service',
            response_model=SystemServiceListModel,
            description=SystemApiDescription.system_service_api
            )
async def get_system_info_service(request: Request,
                                  system_id: int,
                                  db: SystemInfoService = Depends(get_systems)):
    """Get information abuout service for system"""
    return await db.get_system_service_info(request=request, system_id=system_id)
