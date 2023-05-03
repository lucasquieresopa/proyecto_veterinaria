from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    #mail = models.EmailField    #.foreignKey ??
    name = models.SlugField()   #slug es texto corto
    #surname = models.SlugField()
    #address = models.TextField('')
    #tel = models.TextField('')