from pydantic import BaseModel, Field


class CategoryModel(BaseModel):
    id: int
    name: str
    description: str


class PaginateCategoryModel(BaseModel):
    result: list[CategoryModel]
    page: int
    limit: int
    count: int


class CategoryErrorModel(BaseModel):
    type: str = Field(default='error')
    text: str = Field(default='Error get category info by id.')
