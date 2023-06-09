# Generated by Django 4.2 on 2023-05-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                error_messages={
                    "unique": "El mail ya se encuentra registrado. Por favor ingrese otro."
                },
                max_length=40,
                unique=True,
                verbose_name="email",
            ),
        ),
    ]
