from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, computed_field
from datetime import timedelta

class Settings(BaseSettings):
    PROJECT_NAME: str = "Menstrual Tracking API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API
    API_V1_STR: str = "/api/v1"

    # CORS
    CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]  # Frontend URL

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "menstrual_tracking"
    POSTGRES_PORT: str = "5432"

    @computed_field
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"  # Generate a secure key for production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @computed_field
    def ACCESS_TOKEN_EXPIRE_DELTA(self) -> timedelta:
        return timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

    # OpenRouter API
    OPENROUTER_API_KEY: str = ""
    OPENROUTER_API_URL: str = "https://openrouter.ai/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
