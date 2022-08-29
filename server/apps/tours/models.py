from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Tour(models.Model):
    tour_name = models.CharField(max_length=15, unique=True)
    tour_price = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(400)])
    tour_description = models.CharField(max_length=100)
    max_participants = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(25)])
    tour_duration = models.IntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(20)])

    def __str__(self) -> str:
        return f"""Pk: {self.pk}, Tour Name: {self.tour_name}, 
        Tour Price: {self.tour_price}, Tour Description: {self.tour_description}, 
       Tour Duration: {self.tour_duration}, Max Participants: {self.max_participants}"""
