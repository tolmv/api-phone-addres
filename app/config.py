import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_TITLE: str = "Phone-Address API"
    API_VERSION: str = "1.0.0"
    
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB: int = int(os.getenv("REDIS_DB", 0))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")
    
    class Config:
        env_file = ".env"

settings = Settings() 