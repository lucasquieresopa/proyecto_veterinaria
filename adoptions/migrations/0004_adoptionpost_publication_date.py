# Generated by Django 4.2 on 2023-06-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adoptions", "0003_adoptionpost_is_adopted"),
    ]

    operations = [
        migrations.AddField(
            model_name="adoptionpost",
            name="publication_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
