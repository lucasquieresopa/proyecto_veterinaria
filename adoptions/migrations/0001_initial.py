# Generated by Django 4.2 on 2023-05-30 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AdoptionPost",
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
                ("name", models.CharField(max_length=30)),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "sex",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Hembra", "Hembra")],
                        max_length=10,
                    ),
                ),
                (
                    "breed",
                    models.CharField(
                        choices=[
                            ("Sin raza", "Sin Raza"),
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
                        blank=True,
                        choices=[
                            ("Blanco", "Blanco"),
                            ("Negro", "Negro"),
                            ("Marrón", "Marron"),
                            ("Blanco y negro", "Blanco Y Negro"),
                            ("Otro color", "Otro"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Grande", "Grande"),
                            ("Mediano", "Mediano"),
                            ("pequeño", "Pequeño"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "origin",
                    models.CharField(
                        choices=[
                            ("Calle", "Calle"),
                            ("Refugio", "Refugio"),
                            ("Criadero", "Criadero"),
                            ("Hogar", "Hogar"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=120, null=True),
                ),
                (
                    "author",
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
