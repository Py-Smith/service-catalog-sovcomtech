from http import HTTPStatus
from uuid import UUID
from sqlalchemy import select, text

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from core.descriptions import PagingDescription as PageDescr, FilmApiDescription as FilmDescr
from core.messages import FilmMessage
from db.postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from services.system import  SystemInfoService, get_systems

from models.database.system import System
router = APIRouter()


@router.get('/', description='test')
async def get_systems_service(db: SystemInfoService = Depends(get_systems)):
    return await db.get_all_systems()

@router.get('/{system_id}', description='test2')
async def get_system_info_service(system_id: int, db: SystemInfoService = Depends(get_systems)):
    return await db.get_system_info(system_id)