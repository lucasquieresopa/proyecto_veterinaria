# Generated by Django 4.2 on 2023-05-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_remove_customuser_shift"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=40, unique=True, verbose_name="email"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="telephone",
            field=models.SlugField(blank=True, max_length=15, null=True),
        ),
    ]
