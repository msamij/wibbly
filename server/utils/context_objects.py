from typing import Generic, TypeVar

from django.db import models

from server.apps.ratings.models import Rating

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

    def get_context_obj_images(self, image_model_obj: T) -> list:
        return [images for images in image_model_obj[:4]]

    def get_context_obj_rating(self, rating_model_obj: T) -> list:
        return [Rating.objects.filter(pk=target_obj.rating.pk)[0] for target_obj in rating_model_obj[:4]]
