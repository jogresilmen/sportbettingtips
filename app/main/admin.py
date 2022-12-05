# Librerias Django
# Django Libraries
from django.contrib import admin

# Local Folders Libraries
from .models import Glosary

# Register your models here.


@admin.register(Glosary)
class GlosaryAdmin(admin.ModelAdmin):
    pass
