from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey

from django.contrib.auth.models import User

import time

# Create your models here.

class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = DateTimeField(auto_now_add=True)
    name = CharField(max_length=100)
    current_city = CharField(max_length=200)
    profile_picture = CharField(max_length=2000, default="https://media1.thehungryjpeg.com/thumbs2/ori_3686943_09tpyqe6r67ba765aheypmgvqo0vltfraf4ru77u_plane-icon.jpg")