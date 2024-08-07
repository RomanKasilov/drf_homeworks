from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.cars.choices.body_type_choice import BodyTypeChoice


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=255, validators=(V.MinLengthValidator(2),))
    price = models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(1_000_000)))
    year = models.IntegerField(validators=(V.MinValueValidator(1950), V.MaxValueValidator(datetime.now().year)))
    body_type = models.CharField(max_length=9, choices=BodyTypeChoice.choices)
