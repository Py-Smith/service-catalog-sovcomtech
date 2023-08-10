from pydantic import BaseConfig


class Settings(BaseConfig):

    project_name: str = 'movies'

    redis_host: str = '127.0.0.1'
    redis_port: int = 6379

    elastic_schema: str = 'http://'
    elastic_host: str = '127.0.0.1'
    elastic_port: int = 9200

    cache_expire_in_seconds: int = 300


settings = Settings()
