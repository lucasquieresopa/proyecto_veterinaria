from django.db import models
from accounts.models import CustomUser

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
    target_date = models.DateTimeField(
        blank=True,
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