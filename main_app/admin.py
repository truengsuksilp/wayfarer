from django.contrib import admin

from .models import Profile, Post, City

# Register your models here.
admin.site.register([Profile, Post, City])