# Generated by Django 4.2 on 2023-06-02 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("adoptions", "0004_adoptionpost_publication_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adoptionpost",
            name="publication_date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
