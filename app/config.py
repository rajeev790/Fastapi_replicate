from pydantic import BaseSettings

class Settings(BaseSettings):
    replicate_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()
