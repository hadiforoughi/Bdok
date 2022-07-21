from decouple import config
from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    API_V1_STR: str = "/api/va"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY",cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7   # 7 days
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "BDok"

    # Database
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    
    class Config:
        case_sensitive = True
        
settings = Settings()