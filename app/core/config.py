import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "MliChat"
    app_version: str = "1.0.0"
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    secret_key: str = os.getenv("SECRET_KEY", "mlichat-secret-key-change-in-production")


settings = Settings()
