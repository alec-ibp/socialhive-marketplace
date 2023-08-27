from __future__ import annotations

from typing import Any

from abc import ABC, abstractmethod

from src.marketplace.domain.models import Product
from . import repository
from .db import get_redis_connection


class AbstractUnitOfWork(ABC):
    product: repository.AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args) -> AbstractUnitOfWork:
        self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class RedisUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session: Any = None) -> None:
        if not session:
            self.session_factory = get_redis_connection
        else:
            self.session_factory = session

    def __enter__(self):
        self.session = self.session_factory()
        Product._meta.database = self.session
        self.product = repository.ProductRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        return  # TODO check redis transaction
        self.session.commit()

    def rollback(self):
        return  # TODO check redis transaction
        self.session.rollback()
