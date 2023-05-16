from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Dog(models.Model):

    class Sex(models.TextChoices):
        male = "Macho"
        female = "Hembra"
    
    class Breed(models.TextChoices):
        no_breed = "Sin raza"
        has_breed = "De raza"

    name = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=Sex.choices)
    breed = models.CharField(max_length=20, choices=Breed.choices)
    owner = models.IntegerField("Dueño", blank=False, default=1)
    
