from django.contrib import admin
# TODO from .models import {Model}

from .models import Profile, Post, City, Comment

# Prepopulate slug fields when name
# Reference: https://learndjango.com/tutorials/django-slug-tutorial
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'join_date', 'name', 'current_city', 'profile_picture',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Profile)
admin.site.register([Post, City, Comment])



