from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user', 'sofo_name']

admin.site.register(Profile, ProfileAdmin)

