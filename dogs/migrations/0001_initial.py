# Generated by Django 4.2 on 2023-05-19 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dogs.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Dog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=15)),
                ("age", models.PositiveIntegerField()),
                (
                    "sex",
                    models.CharField(
                        choices=[("Macho", "Male"), ("Hembra", "Female")], max_length=10
                    ),
                ),
                (
                    "breed",
                    models.CharField(
                        choices=[
                            ("Sin raza", "No Breed"),
                            ("Coker", "Coker"),
                            ("Pastor aleman", "Pastor Aleman"),
                            ("Bulldog", "Bulldog"),
                            ("Labrador", "Labrador"),
                            ("Golder", "Golden"),
                            ("Caniche", "Caniche"),
                            ("Chihuahua", "Chihuahua"),
                            ("Bulldog Frances", "Bulldog Frances"),
                            ("Beagle", "Beagle"),
                            ("Boxer", "Boxer"),
                            ("Galgo", "Galgo"),
                            ("Dalmata", "Dalmata"),
                            ("Shar pei", "Sharpei"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("Blanco", "White"),
                            ("Negro", "Black"),
                            ("Marrón", "Brown"),
                            ("Blanco y negro", "Black And White"),
                            ("Otro color", "Other"),
                        ],
                        default=dogs.models.Dog.default_value,
                        max_length=20,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        default=dogs.models.Dog.default_value, max_length=10
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default=dogs.models.Dog.default_value, max_length=100
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
