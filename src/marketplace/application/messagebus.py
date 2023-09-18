from __future__ import annotations

import requests
from dataclasses import asdict
from typing import Any

from config import settings
from src.marketplace.domain.events import Event, CreateOrder


def handler(event: Event, by_batch: bool = False) -> Any:
    if by_batch:
        for handler in HANDLERS[type(event)]:
            handler(event)
    else:
        return HANDLERS[type(event)](event)


def create_order_event(event: CreateOrder) -> None:
    request_body: dict = asdict(event)
    response = requests.post(f"{settings.BASE_PAYMENTS_API}/payments/", json=request_body)
    # TODO catch errors of response


HANDLERS: dict[Event, callable] = {
    CreateOrder: create_order_event
}
