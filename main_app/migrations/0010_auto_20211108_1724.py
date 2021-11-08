# Generated by Django 3.1.2 on 2021-11-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='no_slugs', max_length=100, unique=True),
        ),
    ]
