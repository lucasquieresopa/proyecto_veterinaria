# Generated by Django 4.2 on 2023-06-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adoptions", "0002_alter_adoptionpost_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="adoptionpost",
            name="is_adopted",
            field=models.BooleanField(default=False),
        ),
    ]
