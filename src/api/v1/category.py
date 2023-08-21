from fastapi import APIRouter, Depends, Request

from services.category import SystemCategoryInfoService, get_categories

router = APIRouter()


@router.get('/', description='name1')
async def get_all_categories(request: Request,
                             db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about all categories"""
    return await db.get_all_categories(request=request)


@router.get('/{category_id}', description='name')
async def get_category_info_by_id(request: Request,
                                  category_id: int,
                                  db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about categories by id"""
    return await db.get_category_info_by_id(request=request, category_id=category_id)


@router.get('/{category_id}/system', description='name')
async def get_system_category_by_id(request: Request,
                                    category_id: int,
                                    db: SystemCategoryInfoService = Depends(get_categories)):
    """Get information about categories by id"""
    return await db.get_system_category_by_id(request=request, category_id=category_id)
