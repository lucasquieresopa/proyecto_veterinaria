# Generated by Django 4.2 on 2023-06-09 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("perdidos", "0003_alter_lostpost_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="lostpost",
            name="publication_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
