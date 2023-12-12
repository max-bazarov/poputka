from app.config import Settings


class AuthSettings(Settings):
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 7  # 7 days
    REFRESH_TOKEN_KEY: str
    ACCESS_TOKEN_EXP: int = 60 * 60  # 1 hour
    ACCESS_TOKEN_KEY: str

    JWT_ALG: str
    JWT_SECRET: str

    SECURE_COOKIES: bool = True


auth_settings = AuthSettings()
