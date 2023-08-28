from pydantic import BaseModel


class SystemModel(BaseModel):
    id: int
    name: str
    description: str


class PaginateSystemModel(BaseModel):
    result: list[SystemModel]
    page: int
    limit: int
    count: int
