from pydantic import BaseModel


class MainTeamsModel(BaseModel):
    id: int
    role_id: int
    role_name: str
    plan_time: float
    pyrus_stage: int
    start_support_time: float
    end_support_time: float


class CompetenceTeamsModel(BaseModel):
    id: int
    role_id: int
    role_name: str
    plan_time: float
    pyrus_stage: int
    start_support_time: float
    end_support_time: float


class MainTeamsListModel(BaseModel):
    result: list[MainTeamsModel] | None


class CompetenceTeamsListModel(BaseModel):
    result: list[CompetenceTeamsModel] | None
