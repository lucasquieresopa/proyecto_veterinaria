# Generated by Django 4.2 on 2023-05-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dogs", "0003_alter_vaccination_applied_dose"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vaccination",
            name="applied_dose",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]