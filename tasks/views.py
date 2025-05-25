from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
import json

from .models import Categoria, Etiqueta, Tarea
from .forms import TareaForm, CategoriaForm, EtiquetaForm

def index(request):
    """Vista principal que muestra todas las tareas"""
    categorias = Categoria.objects.all()
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    
    context = {
        'categorias': categorias,
        'tareas': tareas,
    }
    return render(request, 'tasks/index.html', context)

def categoria_detail(request, categoria_id):
    """Vista que muestra las tareas de una categoría específica"""
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=categoria_id)
    tareas = Tarea.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    
    context = {
        'categorias': categorias,
        'categoria': categoria,
        'tareas': tareas,
    }
    return render(request, 'tasks/categoria_detail.html', context)

def tarea_detail(request, tarea_id):
    """Vista que muestra el detalle de una tarea"""
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    context = {
        'tarea': tarea,
    }
    return render(request, 'tasks/tarea_detail.html', context)

def tarea_create(request):
    """Vista para crear una nueva tarea"""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea creada con éxito')
            return redirect('tasks:index')
    else:
        form = TareaForm()
    
    context = {
        'form': form,
        'categorias': Categoria.objects.all(),
        'etiquetas': Etiqueta.objects.all(),
    }
    return render(request, 'tasks/tarea_form.html', context)

def tarea_update(request, tarea_id):
    """Vista para actualizar una tarea existente"""
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada con éxito')
            return redirect('tasks:tarea_detail', tarea_id=tarea.id)
    else:
        form = TareaForm(instance=tarea)
    
    context = {
        'form': form,
        'tarea': tarea,
        'categorias': Categoria.objects.all(),
        'etiquetas': Etiqueta.objects.all(),
    }
    return render(request, 'tasks/tarea_form.html', context)

def tarea_delete(request, tarea_id):
    """Vista para eliminar una tarea"""
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        tarea.delete()
        messages.success(request, 'Tarea eliminada con éxito')
        return redirect('tasks:index')
    
    context = {
        'tarea': tarea,
    }
    return render(request, 'tasks/tarea_confirm_delete.html', context)

def tarea_toggle_complete(request, tarea_id):
    """Vista para marcar/desmarcar una tarea como completada"""
    tarea = get_object_or_404(Tarea, id=tarea_id)
    
    if request.method == 'POST':
        # Para peticiones AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = json.loads(request.body)
            tarea.completada = data.get('completada', not tarea.completada)
            tarea.save()
            return JsonResponse({'success': True, 'completada': tarea.completada})
        
        # Para peticiones normales
        tarea.completada = not tarea.completada
        tarea.save()
        messages.success(request, f'Tarea marcada como {"completada" if tarea.completada else "pendiente"}')
        return redirect(request.META.get('HTTP_REFERER', 'tasks:index'))
    
    return redirect('tasks:tarea_detail', tarea_id=tarea.id)

def categorias_list(request):
    """Vista que muestra todas las categorías"""
    categorias = Categoria.objects.all()
    
    context = {
        'categorias': categorias,
    }
    return render(request, 'tasks/categorias_list.html', context)

def categoria_create(request):
    """Vista para crear una nueva categoría"""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada con éxito')
            return redirect('tasks:categorias')
    else:
        form = CategoriaForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tasks/categoria_form.html', context)

def categoria_update(request, categoria_id):
    """Vista para actualizar una categoría existente"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada con éxito')
            return redirect('tasks:categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {
        'form': form,
        'categoria': categoria,
    }
    return render(request, 'tasks/categoria_form.html', context)

def categoria_delete(request, categoria_id):
    """Vista para eliminar una categoría"""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoría eliminada con éxito')
        return redirect('tasks:categorias')
    
    context = {
        'categoria': categoria,
    }
    return render(request, 'tasks/categoria_confirm_delete.html', context)

def etiquetas_list(request):
    """Vista que muestra todas las etiquetas"""
    etiquetas = Etiqueta.objects.all()
    
    context = {
        'etiquetas': etiquetas,
    }
    return render(request, 'tasks/etiquetas_list.html', context)

def etiqueta_create(request):
    """Vista para crear una nueva etiqueta"""
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada con éxito')
            return redirect('tasks:etiquetas')
    else:
        form = EtiquetaForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tasks/etiqueta_form.html', context)

def etiqueta_update(request, etiqueta_id):
    """Vista para actualizar una etiqueta existente"""
    etiqueta = get_object_or_404(Etiqueta, id=etiqueta_id)
    
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada con éxito')
            return redirect('tasks:etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    
    context = {
        'form': form,
        'etiqueta': etiqueta,
    }
    return render(request, 'tasks/etiqueta_form.html', context)

def etiqueta_delete(request, etiqueta_id):
    """Vista para eliminar una etiqueta"""
    etiqueta = get_object_or_404(Etiqueta, id=etiqueta_id)
    
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada con éxito')
        return redirect('tasks:etiquetas')
    
    context = {
        'etiqueta': etiqueta,
    }
    return render(request, 'tasks/etiqueta_confirm_delete.html', context)
