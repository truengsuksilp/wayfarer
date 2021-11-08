# Generated by Django 3.2.8 on 2021-11-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(default='no_slugs', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='no_slugs', max_length=100, unique=True),
        ),
    ]
