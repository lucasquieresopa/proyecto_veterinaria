# Generated by Django 4.2 on 2023-05-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shift',
            options={'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
        migrations.AddField(
            model_name='shift',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
