from django.contrib import admin
from .models import Place, Review
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['place_name']

admin.site.register(Place, PlaceAdmin)
admin.site.register(Review)