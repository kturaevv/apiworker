from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database: str = Field(..., env='POSTGRES_DATABASE')
    username: str = Field(..., env='POSTGRES_USERNAME')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    host: str = Field(..., env='POSTGRES_HOST')
    port: str = Field(..., env='POSTGRES_PORT')

    rabbitmq_host: str = Field(..., env='RABBITMQ_HOST')
    rabbitmq_port: str = Field(..., env='RABBITMQ_PORT')
    
    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
