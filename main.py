import uvicorn

from config import settings
from config.asgi import get_asgi_application


app = get_asgi_application()


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=settings.DEBUG,
        workers=1,
    )
