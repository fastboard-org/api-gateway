from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_host: str
    app_port: int
    users_service_url: str
    dashboards_service_url: str
    firebase_api_key: str
    allowed_origin: str

    class Config:
        env_file = ".env"


settings = Settings()
