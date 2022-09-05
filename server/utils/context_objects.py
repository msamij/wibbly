from typing import Generic, TypeVar

from django.db import models

T = TypeVar('T', models.Model, models.Model)


class Context(Generic[T]):

    def __init__(self, model_type: T, key_value: str) -> None:
        self._context_obj = model_type.objects.filter(name=key_value)

    def get_context_obj(self) -> T:
        return self._context_obj[0]

    def get_context_obj_name(self) -> list:
        return self.get_context_obj().name

    def get_context_obj_description(self) -> list:
        return self.get_context_obj().description

    def get_context_obj_price(self) -> list:
        return self.get_context_obj().price
