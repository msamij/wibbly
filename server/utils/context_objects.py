from abc import ABC
from typing import Generic, TypeVar

from django.db import models

T = TypeVar('T', models.Model, models.Model)


class Context(Generic[T]):

    def __init__(self) -> None:
        self._context_obj: T = None

    def get_context_obj(self) -> T:
        return self._context_obj[0]
