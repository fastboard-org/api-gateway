from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_host: str
    app_port: int
    users_service_url: str

    class Config:
        env_file = ".env"


settings = Settings()
