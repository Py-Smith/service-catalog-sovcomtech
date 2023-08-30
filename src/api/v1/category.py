from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request

from core.descriptions import CategoryDescription, PagingDescription
from models.response.category import (CategoryErrorModel, CategoryModel,
                                      PaginateCategoryModel)
from models.response.system import SystemListModel
from services.category import SystemCategoryInfoService, get_categories

router = APIRouter()


@router.get('/',
            response_model=PaginateCategoryModel,
            description=CategoryDescription.all_category_api)
async def get_all_categories(request: Request,
                             page: Annotated[int, Query(description=PagingDescription.page)] = 0,
                             limit: Annotated[int, Query(description=PagingDescription.limit)] = 50,
                             db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about all categories"""
    return await db.get_all_categories(request=request, page=page, limit=limit)


@router.get('/{category_id}',
            response_model=CategoryModel | CategoryErrorModel,
            description=CategoryDescription.category_by_id_api)
async def get_category_info_by_id(request: Request,
                                  category_id: int,
                                  db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about categories by id"""
    try:
        return await db.get_category_info_by_id(request=request, category_id=category_id)
    except TypeError:
        return CategoryErrorModel


@router.get('/{category_id}/system',
            response_model=SystemListModel,
            description=CategoryDescription.system_in_category_by_id_api)
async def get_system_category_by_id(request: Request,
                                    category_id: int,
                                    db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about categories by id"""
    return await db.get_system_category_by_id(request=request, category_id=category_id)
