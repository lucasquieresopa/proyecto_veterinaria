# Generated by Django 4.2.1 on 2023-05-28 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_appointment_dog'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='mandado',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
        ),
    ]