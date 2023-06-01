from django.db import models
from accounts.models import CustomUser
from dogs.models import Dog

class AdoptionPost(models.Model):

    class Origin(models.TextChoices):
        calle = "Calle"
        refugio = "Refugio"
        criadero = "Criadero"
        hogar = "Hogar"


    author = models.ForeignKey(
        CustomUser,
        blank = True,
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField(
        max_length=30,
    )
    age = models.CharField(
        null=True,
        blank=True,
        max_length=30, 
    )
    sex = models.CharField(
        max_length=10, 
        choices=Dog.Sex.choices
    )
    breed = models.CharField(
        max_length=20, 
        choices=Dog.Breed.choices
    )
    color = models.CharField(
        max_length=20, 
        blank=True, 
        choices=Dog.Color.choices, 
        null=True, 
    )
    size = models.CharField(
        max_length=10,
        null=True, 
        blank=True, 
        choices=Dog.Size.choices, 
    )
    origin = models.CharField(
        max_length=20,
        choices=Origin.choices,
    )
    description = models.TextField(
        max_length=120,
        blank=True, 
        null=True, 
    )
    is_adopted = models.BooleanField(
        default=False,
    )
