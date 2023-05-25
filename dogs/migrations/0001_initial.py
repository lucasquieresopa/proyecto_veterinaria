# Generated by Django 4.2 on 2023-05-24 19:44

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                ("name", models.CharField(max_length=30)),
                (
                    "date_of_birth",
                    models.DateField(
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                datetime.date.today,
                                "La fecha de nacimiento del perro debe ser anterior a hoy",
                            )
                        ],
                    ),
                ),
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
                ("size", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=120, null=True),
                ),
                ("hidden", models.BooleanField(default=False)),
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
        migrations.CreateModel(
            name="Vaccination",
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
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Antirrabica", "Antirrabica"),
                            ("Antimoquillo", "Antimoquillo"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "brand",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                20,
                                message="El nombre de la marca no puede superar los 20 caracteres",
                            )
                        ],
                    ),
                ),
                (
                    "lot",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                14,
                                message="El nombre del lote no puede superar los 15 caracteres",
                            )
                        ],
                    ),
                ),
                ("dosis_number", models.PositiveIntegerField(null=True)),
                ("total_dosis", models.PositiveIntegerField(null=True)),
                (
                    "date_of_application",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                datetime.date.today,
                                message="La fecha de atención debe ser anterior a la fecha de hoy",
                            )
                        ],
                    ),
                ),
                (
                    "dog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dogs.dog",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attention",
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
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Radiografia", "Radiografia"),
                            ("Primeros auxilios", "Primeros Auxilios"),
                            ("Operacion", "Operacion"),
                            ("Otros Servicios", "Otros Servicios"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=120,
                        null=True,
                        validators=[
                            django.core.validators.MaxLengthValidator(
                                120,
                                message="La descripción debe tener a lo sumo 120 caracteres",
                            )
                        ],
                    ),
                ),
                (
                    "date_of_attention",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(
                                datetime.date.today,
                                message="La fecha de atención debe ser anterior a la fecha de hoy",
                            )
                        ],
                    ),
                ),
                (
                    "dog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dogs.dog",
                    ),
                ),
            ],
        ),
    ]
