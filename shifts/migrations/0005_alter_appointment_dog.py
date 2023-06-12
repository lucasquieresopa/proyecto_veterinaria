# Generated by Django 4.2 on 2023-06-12 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dogs", "0006_vaccination_suggestions"),
        ("shifts", "0004_alter_appointment_mandado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="dog",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dogs.dog",
            ),
        ),
    ]