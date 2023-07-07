# Generated by Django 4.2 on 2023-07-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("donations", "0002_alter_campaign_target_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                    "email",
                    models.EmailField(max_length=40, unique=True, verbose_name="email"),
                ),
            ],
        ),
    ]