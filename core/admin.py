from django.contrib import admin
from .models import *
# aca vamos a mostrar las tablas en el admin
admin.site.register(Persona)
admin.site.register(Sexo)