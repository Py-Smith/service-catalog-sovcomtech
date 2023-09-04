from fastapi import APIRouter, Depends, Request

from core.descriptions import FormsDescription
from models.response.forms import FormModel, FormsErrorModel, FromsListModel
from services.forms import FormsService, get_forms

router = APIRouter()


@router.get('/{form_id}',
            response_model=FormModel | FormsErrorModel,
            description=FormsDescription.form_by_id_api
            )
async def get_form_info_by_id(request: Request,
                              form_id: int,
                              db: FormsService = Depends(get_forms)):
    """Get information about form by id"""
    try:
        return await db.get_forms_by_id(request=request, form_id=form_id)
    except TypeError:
        return FormsErrorModel


@router.get('/system_service/{system_service_id}',
            response_model=FromsListModel,
            description=FormsDescription.form_by_system_service_id_api
            )
async def get_forms_by_system_service_id(request: Request,
                                         system_service_id: int,
                                         db: FormsService = Depends(get_forms)):
    """Get information abuout form by system service id"""
    return await db.get_forms_by_system_service_id(request=request,
                                                   system_service_id=system_service_id)
