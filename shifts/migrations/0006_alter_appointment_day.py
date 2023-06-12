# Generated by Django 4.2 on 2023-06-12 15:22

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0005_alter_appointment_dog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="day",
            field=models.DateField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        datetime.date.today,
                        message="La fecha del turno debe ser despues de la fecha de hoy",
                    )
                ],
            ),
        ),
    ]