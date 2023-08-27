from config import settings

from redis import Redis
from redis_om.connections import get_redis_connection


def get_redis_session() -> Redis:
    return get_redis_connection(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
    )
