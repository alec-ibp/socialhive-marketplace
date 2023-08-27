from __future__ import annotations

import importlib
from functools import lru_cache


SETTINGS_MODULE: str = 'config.service_settings'


class ServiceSettings:
    def __init__(self) -> None:
        module = importlib.import_module(SETTINGS_MODULE)

        tuple_settings: tuple[str] = (
            "ALLOWED_HOSTS",
            "INSTALLED_APPS",
            "CORS_ALLOWED_METHODS",
            "CORS_ALLOWED_HEADERS",
        )

        self._explicit_settings: set[str] = set()

        for setting in dir(module):
            if setting.isupper():
                setting_value = getattr(module, setting)
                if setting in tuple_settings and not isinstance(setting_value, (tuple, list)):
                    raise ValueError(f"{setting} must be a tuple or list")
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)


@lru_cache()
def get_settings() -> ServiceSettings:
    return ServiceSettings()


settings: ServiceSettings = get_settings()
