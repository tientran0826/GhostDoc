from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "GhostDoc"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    POSTGRES_GHOSTDOC_DB: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    REDIS_URL: str | None = None

    LANGFUSE_HOST: str
    LANGFUSE_PUBLIC_KEY: str
    LANGFUSE_SECRET_KEY: str

    @property
    def GHOSTDOC_DB_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_GHOSTDOC_DB}"

    @property
    def LANGFUSE_DB_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    SESSION_EXPIRE_DAYS: int = 7


settings = Settings()
