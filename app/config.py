from pydantic import BaseSettings, Field

from functools import lru_cache


class Settings(BaseSettings):
    database: str = Field(..., env='POSTGRES_DATABASE')
    username: str = Field(..., env='POSTGRES_USERNAME')
    password: str = Field(..., env='POSTGRES_PASSWORD')
    host: str = Field(..., env='POSTGRES_HOST')

    class Config:
        env_file = '.env'
        
@lru_cache
def get_settings():
    return Settings()