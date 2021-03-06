# Generated by Django 3.1.2 on 2021-11-08 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='no_slugs', max_length=100)),
                ('country', models.CharField(max_length=250)),
                ('picture', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='no_slugs', max_length=100)),
                ('current_city', models.CharField(max_length=200)),
                ('profile_picture', models.CharField(default='https://media1.thehungryjpeg.com/thumbs2/ori_3686943_09tpyqe6r67ba765aheypmgvqo0vltfraf4ru77u_plane-icon.jpg', max_length=2000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=48)),
                ('content', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.city')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.profile')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
