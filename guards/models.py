from django.db import models
from accounts.models import CustomUser
from datetime import datetime, date
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from dateutil import relativedelta

class Guards(models.Model):


    vet = models.CharField(
        max_length=30,
        validators=[MaxLengthValidator(30, message="El nombre de la veterinaria no puede superar los 20 caracteres")],
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=30,
        validators=[MaxLengthValidator(30, message="La direccion no puede superar los 15 caracteres")],
        blank=True,
        null=True
    )
    
    date_of_guards = models.DateField(
        null=True,

        validators=[ MinValueValidator(date.today, message="La fecha de guardia no debe ser anterior a la fecha de hoy")],
    )
    


def __str__(self):
        return f" | day: {self.date_of_guards} | guard: {self.vet} | address: {self.address} |"


