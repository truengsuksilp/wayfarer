# Generated by Django 3.1.2 on 2021-11-08 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_city_slug_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='slug_field',
            new_name='slug',
        ),
    ]