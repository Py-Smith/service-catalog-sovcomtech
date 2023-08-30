from pydantic import BaseModel, Field


class SystemModel(BaseModel):
    id: int
    name: str
    description: str


class SystemListModel(BaseModel):
    result: list[SystemModel]


class PaginateSystemModel(BaseModel):
    result: list[SystemModel]
    page: int
    limit: int
    count: int


class SystemErrorModel(BaseModel):
    type: str = Field(default='error')
    text: str = Field(default='Error get system info by id.')


class Service(BaseModel):
    id: int
    name: str
    description: str
    time_to_request: float
    start_support_time: float
    end_support_time: float
    method_providing: str


class Owner(BaseModel):
    id: int
    name: str
    pyrus_id: int
    email: str
    department: str
    management: str
    divizion: str


class Calendar(BaseModel):
    id: int
    name: str
    description: str


class SystemServiceModel(BaseModel):
    id: int
    system_name: str
    service: Service
    owner: Owner
    calendar: Calendar


class SystemServiceListModel(BaseModel):
    result: list[SystemServiceModel] | None
