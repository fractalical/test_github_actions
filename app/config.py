from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    POSTGRES_HOST: str = "course-postgres"
    POSTGRES_PORT: int = 5432

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
