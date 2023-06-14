from pydantic import BaseSettings


class AuthConfig(BaseSettings):
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 7  # 7 days
    ACCESS_TOKEN_EXP: int = 60 * 60  # 1 hour
    ACCESS_TOKEN_KEY: str

    JWT_ALG: str
    JWT_SECRET: str

    SECURE_COOKIES: bool = True

    class Config:
        env_file = '.env'


config = AuthConfig()
