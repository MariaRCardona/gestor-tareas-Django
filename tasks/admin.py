from django.contrib import admin
from .models import Categoria, Etiqueta, Tarea

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'color', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')
    search_fields = ('nombre',)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'prioridad', 'fecha_vencimiento', 'completada')
    list_filter = ('completada', 'prioridad', 'categoria', 'etiquetas')
    search_fields = ('titulo', 'descripcion')
    filter_horizontal = ('etiquetas',)
    date_hierarchy = 'fecha_creacion'
