from django.contrib import admin
# TODO from .models import {Model}

from .models import Profile, Post, City

# Register your models here.
admin.site.register([Profile, Post, City])
