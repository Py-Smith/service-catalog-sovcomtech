from pydantic import BaseModel, Field


class FormModel(BaseModel):
    id: int
    form_id: int
    form_name: str


class FromsListModel(BaseModel):
    result: list[FormModel] | None


class FormsErrorModel(BaseModel):
    type: str = Field(default='error')
    text: str = Field(default='Error get form info by id.')
