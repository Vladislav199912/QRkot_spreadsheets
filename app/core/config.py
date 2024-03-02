from pydantic import BaseSettings

from app.core.constants import APP_INFO, APP_TITLE, DATABASE_URL, SECRET


class Settings(BaseSettings):
    app_title: str = APP_TITLE
    app_info: str = APP_INFO
    database_url: str = DATABASE_URL
    secret: str = SECRET

    class Config:
        env_file = '.env'


settings = Settings()
