from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Vistas principales
    path('', views.index, name='index'),
    path('categoria/<int:categoria_id>/', views.categoria_detail, name='categoria_detail'),
    path('tarea/<int:tarea_id>/', views.tarea_detail, name='tarea_detail'),
    
    # Gestión de tareas
    path('tarea/nueva/', views.tarea_create, name='tarea_create'),
    path('tarea/<int:tarea_id>/editar/', views.tarea_update, name='tarea_update'),
    path('tarea/<int:tarea_id>/eliminar/', views.tarea_delete, name='tarea_delete'),
    path('tarea/<int:tarea_id>/completar/', views.tarea_toggle_complete, name='tarea_toggle_complete'),
    
    # Gestión de categorías
    path('categorias/', views.categorias_list, name='categorias'),
    path('categoria/nueva/', views.categoria_create, name='categoria_create'),
    path('categoria/<int:categoria_id>/editar/', views.categoria_update, name='categoria_update'),
    path('categoria/<int:categoria_id>/eliminar/', views.categoria_delete, name='categoria_delete'),
    
    # Gestión de etiquetas
    path('etiquetas/', views.etiquetas_list, name='etiquetas'),
    path('etiqueta/nueva/', views.etiqueta_create, name='etiqueta_create'),
    path('etiqueta/<int:etiqueta_id>/editar/', views.etiqueta_update, name='etiqueta_update'),
    path('etiqueta/<int:etiqueta_id>/eliminar/', views.etiqueta_delete, name='etiqueta_delete'),
]
