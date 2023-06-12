from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from accounts.models import CustomUser
from dogs.models import Dog




SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
)

TIME_CHOICES = (
    ("Mañana", "Mañana"),
    ("Tarde", "Tarde"),
)
STATUS_CHOICES = (
    ("Pendiente", "Pendiente"),
    ("Confirmado", "Confirmado"),
    ("Cancelado", "Cancelado"),
)
class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True) 
    #service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="Mañana")
    description = models.CharField(max_length=200, blank=True)
    #dog = models.CharField(max_length=50, blank=True)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=50, default="Pendiente")
    mandado = models.CharField(max_length=50, default="1") 
    def __str__(self):
        return f" | day: {self.day} | time: {self.time} | user: {self.user.email} |"


