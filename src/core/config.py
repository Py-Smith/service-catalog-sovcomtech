
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    project_name: str = Field(..., env='PROJECT_NAME')

    db_host: str = Field(..., env='DB_HOST')
    db_port: int = Field(..., env='DB_PORT')
    db_user: str = Field(..., env='DB_USER')
    db_password: str = Field(..., env='DB_PASSWORD')
    db_name: str = Field(..., env='DB_NAME')

    redis_host: str = Field(..., env='REDIS_HOST')
    redis_port: str = Field(..., env='REDIS_PORT')

    redis_ex: int = Field(400, env='REDIS_EX')

    class Config:
        env_file = ".env"


settings: Settings = Settings()
