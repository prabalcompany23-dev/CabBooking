from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = "sqlite:///./book_a_ride.db"
    secret_key: str = "dev-secret-change-in-env"
    pilot_city: str = "Bengaluru"
    pilot_sport: str = "Badminton"
    ops_username: str = "ops"
    ops_password: str = "ops-demo-change-me"


@lru_cache
def get_settings() -> Settings:
    return Settings()
