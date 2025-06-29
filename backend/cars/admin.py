from django.contrib import admin
from .models import Cars

class CarsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cars, CarsAdmin)