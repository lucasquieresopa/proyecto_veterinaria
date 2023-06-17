from datetime import date
from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator

# Create your models here.

class Campaign(models.Model):

    author = models.ForeignKey(
        CustomUser,
        blank = True,
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.ImageField(
        upload_to= "media/", 
        null = True,
    )
    campaign_name = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=120,
        blank=True, 
        null=True, 
    )
    target_date = models.DateField(
        blank=True,
        validators=[MinValueValidator(date.today, message="La fecha objetivo debe ser posterior a la fecha de hoy")],
    )
    target_money = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    actual_money = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
    )