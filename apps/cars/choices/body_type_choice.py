from django.db import models


class BodyTypeChoice(models.TextChoices):
    HatchBack = 'HatchBack'
    Sedan = 'Sedan',
    Coupe = 'Coupe',
    Wagon = 'Wagon',
    Jeep = 'Jeep',
