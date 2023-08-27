from __future__ import annotations

import os
from distutils.util import strtobool

from dotenv import load_dotenv


load_dotenv()


VERSION: str = "0.1.0"

INSTALLED_APPS: list[str] = [
    "marketplace",
]

DEBUG: bool = bool(strtobool(os.environ.get("DEBUG", "False")))


# CORS
CORS_ALLOWED_METHODS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HEADERS: list[str] = os.environ.get("CORS_ALLOWED_METHODS", "*").split(",")
CORS_ALLOWED_HOSTS: list[str] = os.environ.get("CORS_ALLOWED_HOSTS", "").split(",")

# Redis db
REDIS_HOST: str = os.environ.get("REDIS_HOST")
REDIS_PORT: int = os.environ.get("REDIS_PORT", 6379)
REDIS_PASSWORD: str = os.environ.get("REDIS_PASSWORD")
