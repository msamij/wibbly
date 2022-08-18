from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Activity(models.Model):
    activity_name = models.CharField(max_length=15, unique=True)
    activity_price = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(2500)])
    activity_description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"""Pk: {self.pk}, 
        Activity Name: {self.activity_name}, 
        Activity Price: {self.activity_price}, 
        Activity Description: {self.activity_description}"""
