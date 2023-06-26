from pydantic import BaseSettings


class AuthConfig(BaseSettings):
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 7  # 7 days
    REFRESH_TOKEN_KEY: str
    ACCESS_TOKEN_EXP: int = 60 * 60  # 1 hour
    ACCESS_TOKEN_KEY: str

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: str
    MAIL_SERVER: str
    MAIL_FROM_NAME: str

    JWT_ALG: str
    JWT_SECRET: str

    SECURE_COOKIES: bool = True

    class Config:
        env_file = '.env'


config = AuthConfig()
