from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register([
    Paper,Compound,CompositionPart, Material
    ], admin.ModelAdmin)
