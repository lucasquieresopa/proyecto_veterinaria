from django.db import models
from accounts.models import CustomUser
from dogs.models import Dog

# Create your models here.



class LostPost (models.Model):

    class Age(models.TextChoices):
        cachorro = "Cachorro"
        mediano = "Mediano"
        adulto = "Adulto"

    author = models.ForeignKey(
        CustomUser,
        blank = True,
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.ImageField(
        upload_to= "perros", null = True,
    ) 
    name = models.CharField(
        max_length=30,
    )
    age = models.CharField(
        choices=Age.choices,
        max_length=15, 
    )
    zone = models.CharField(
        max_length=45, 
        help_text= "ingrese la zona en la que se perdió su perro",
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
        choices=Dog.Size.choices
    )

    was_found = models.BooleanField(
        default= False,
    )

