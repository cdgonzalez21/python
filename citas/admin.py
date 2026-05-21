from django.contrib import admin
from .models import Mascota, Cita


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especie', 'raza', 'edad', 'propietario')
    search_fields = ('nombre', 'propietario', 'especie')


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'fecha', 'hora', 'tipo_cita', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('tipo_cita', 'mascota__nombre')