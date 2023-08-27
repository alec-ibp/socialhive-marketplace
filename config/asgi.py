import importlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp

from config import settings


def get_asgi_application() -> ASGIApp:
    app_name: str = "hive marketplace"
    swagger_docs_url = redoc_url = None
    if settings.DEBUG:
        swagger_docs_url = "/docs"
        redoc_url = "/redoc"

    app: ASGIApp = FastAPI(
        title=app_name,
        version=settings.VERSION,
        debug=settings.DEBUG,
        docs_url=swagger_docs_url,
        redoc_url=redoc_url,
        on_startup=[_startup_event],
    )

    _set_urls(app)
    _configure_cors(app)

    return app


def _startup_event() -> None:
    pass


def _set_urls(app: ASGIApp) -> None:
    for _app in settings.INSTALLED_APPS:
        app_urls = importlib.import_module(f"src.{_app}.infrastructure.api.urls")
        if not hasattr(app_urls, "router"):
            raise Exception("missing router")  # MissingAPIRouterError()
        app.include_router(app_urls.router)


def _configure_cors(app: ASGIApp) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=settings.CORS_ALLOWED_METHODS,
        allow_headers=settings.CORS_ALLOWED_HEADERS,
    )
