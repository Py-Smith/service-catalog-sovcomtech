from http import HTTPStatus
from uuid import UUID
from sqlalchemy import select, text

from fastapi import APIRouter, Depends, HTTPException, Query, Request

from core.descriptions import PagingDescription as PageDescr, FilmApiDescription as FilmDescr
from core.messages import FilmMessage
from db.postgres import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from models.database.system import System
router = APIRouter()


@router.get('/', description='test')
async def get_systems(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(System).order_by(System.id.desc()))
    return result.scalars().all()