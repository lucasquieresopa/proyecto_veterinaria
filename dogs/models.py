from django.db import models
from accounts.models import CustomUser
from datetime import datetime, date
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from dateutil import relativedelta

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


    name = models.CharField(
        max_length=30,
    )
    date_of_birth = models.DateField(
        null=True,
        validators=[MaxValueValidator(date.today, "La fecha de nacimiento del perro debe ser anterior a hoy")]
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
    )
    size = models.CharField(
        max_length=10,
        null=True, 
        blank=True, 
    )
    description = models.TextField(
        max_length=120,
        #validators=[MaxLengthValidator(120, message="La descripción debe tener a lo sumo 120 caracteres")],
        blank=True, 
        null=True, 
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
    
    def calculate_age_year(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        
    
    def calculate_age_month(self):
        today = date.today()
        diff = relativedelta.relativedelta(today,self.date_of_birth)
        diff_in_months = diff.months + diff.years * 12
        years = self.calculate_age_year()
        return (diff_in_months - (12 * years))
        
    
    def calculate_age_days(self):
        today = date.today()
        diff = relativedelta.relativedelta(today,self.date_of_birth)
        return diff.days
        
    def calculate_age(self):
        f_años=self.calculate_age_year()
        f_meses=self.calculate_age_month()
        f_dias=self.calculate_age_days()
        if (f_años == 1):
            años= f"{f_años} año"
        else:
            años= f"{f_años} años"
        if (f_meses == 1):
            meses= f"{f_meses} mes"
        else:
            meses= f"{f_meses} meses"
        if (f_dias == 1):
            dias= f"{f_dias} día"
        else:
            dias= f"{f_dias} días"
        return años + " " + meses + " y " + dias


    
class Attention(models.Model):

    class Type(models.TextChoices):

        radiografia = "Radiografia"
        primeros_auxilios = "Primeros auxilios"
        operacion = "Operacion"
        otros_servicios = "Otros Servicios"

    dog = models.ForeignKey(
        Dog,
        blank = True,
        on_delete=models.CASCADE,
        null=True,
    )
    type = models.CharField(
        choices=Type.choices,
        max_length=20,
        null=True,
        blank=True,

    )
    description = models.TextField(
        max_length=120,
        validators=[MaxLengthValidator(120, message="La descripción debe tener a lo sumo 120 caracteres")],
        blank=True,
        null=True
    )
    date_of_attention = models.DateField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(date.today, message="La fecha de atención debe ser anterior a la fecha de hoy")],
    )



class Vaccination(models.Model):

    class Type(models.TextChoices):

        antirrabica = "Antirrabica"
        antimoquillo = "Antimoquillo"

    dog = models.ForeignKey(
        Dog,
        blank = True,
        on_delete=models.CASCADE,
        null=True,
    )
    type = models.CharField(
        choices=Type.choices,
        max_length=20,
        null=True,
        blank=True,

    )
    brand = models.CharField(
        max_length=20,
        validators=[MaxLengthValidator(20, message="El nombre de la marca no puede superar los 20 caracteres")],
        blank=True,
        null=True
    )
    lot = models.CharField(
        max_length=15,
        validators=[MaxLengthValidator(14, message="El nombre del lote no puede superar los 15 caracteres")],
        blank=True,
        null=True
    )
    dosis_number = models.PositiveIntegerField(
        null=True,
    )
    total_dosis = models.PositiveIntegerField(
        null=True,
    )
    date_of_application = models.DateField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(date.today, message="La fecha de atención debe ser anterior a la fecha de hoy")],
    )
