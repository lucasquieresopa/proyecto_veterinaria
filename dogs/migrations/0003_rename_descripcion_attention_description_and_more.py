# Generated by Django 4.2 on 2023-05-21 13:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dogs", "0002_alter_dog_breed_alter_dog_color_alter_dog_sex_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="attention",
            old_name="descripcion",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="attention",
            old_name="tipo",
            new_name="type",
        ),
    ]