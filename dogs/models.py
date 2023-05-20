from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Dog(models.Model):

    class Sex(models.TextChoices):
        macho = "Macho"
        hembra = "Hembra"
    
    class Breed(models.TextChoices):
        sin_raza = "Sin raza"
        coker = "Coker"
        pastor_aleman = "Pastor aleman"
        bulldog = "Bulldog"
        labrador = "Labrador"
        golden = "Golder"
        caniche = "Caniche"
        chihuahua = "Chihuahua"
        bulldog_frances = "Bulldog Frances"
        beagle = "Beagle"
        boxer = "Boxer"
        galgo = "Galgo"
        dalmata = "Dalmata"
        sharpei = "Shar pei"
        #...
    
    class Color(models.TextChoices):
        blanco = "Blanco"
        negro = "Negro"
        marron = "Marrón"
        blanco_y_negro = "Blanco y negro"
        otro = "Otro color"

    class Size(models.TextChoices):
        grande = "Grande"
        mediano = "Mediano"
        pequeño = "pequeño"


    def default_value():
        return '-'
    

    name = models.CharField(
        max_length=15
    )
    age = models.PositiveIntegerField(
        null=True,
    )
    sex = models.CharField(
        max_length=10, 
        choices=Sex.choices
    )
    breed = models.CharField(
        max_length=20, 
        choices=Breed.choices
    )
    color = models.CharField(
        max_length=20, 
        blank=True, 
        choices=Color.choices, 
        null=True, 
        #default=default_value
    )
    size = models.CharField(
        max_length=10,
        null=True, 
        blank=True, 
        #default=default_value
    )
    description = models.TextField(
        max_length=100, 
        blank=True, 
        null=True, 
        #default=default_value
    )
    hidden = models.BooleanField(default=False)
    owner = models.ForeignKey(
        CustomUser, 
        blank=True, 
        on_delete=models.CASCADE, 
        null=True
    )

    def __str__(self) -> str:
        return self.name
    
    

    
