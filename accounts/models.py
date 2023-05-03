from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mail = models.EmailField    #.foreignKey ??
    name = models.TextField('')
    surname = models.TextField('')
    address = models.TextField('')
    tel = models.TextField('')