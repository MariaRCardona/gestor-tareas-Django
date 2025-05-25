# Documentación del Proyecto: Gestor de Tareas con Django

## Descripción General

Este proyecto es un Gestor de Tareas desarrollado con Django, que permite a los usuarios organizar sus actividades diarias mediante categorías y etiquetas. La aplicación cuenta con una interfaz moderna y atractiva, y cumple con todos los requisitos establecidos en la prueba final del curso básico de Django.

## Características Principales

- Gestión completa de tareas (crear, ver, editar, eliminar)
- Organización por categorías personalizables
- Sistema de etiquetas para clasificación adicional
- Priorización de tareas (baja, media, alta)
- Fechas de vencimiento para seguimiento temporal
- Interfaz responsiva y moderna
- Operaciones CRUD completas

## Requisitos Técnicos Cumplidos

- **Framework**: Django
- **Rutas/Vistas**: Más de 3 vistas basadas en funciones o clases
- **Plantillas**: Uso de Django Templates con herencia de plantilla base
- **Modelo de datos**: 3 modelos relacionados con el ORM de Django
- **Formularios**: Validación con Django Forms
- **Operaciones CRUD**: Implementadas para todos los modelos
- **Archivos estáticos**: CSS y JS propios

## Estructura del Proyecto

```
gestor_tareas_django/
├── taskmaster/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── static/
│   │   └── tasks/
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── js/
│   │       │   └── main.js
│   │       └── img/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── tarea_detail.html
│   │       ├── tarea_form.html
│   │       ├── tarea_confirm_delete.html
│   │       ├── categoria_detail.html
│   │       ├── categorias_list.html
│   │       ├── categoria_form.html
│   │       ├── categoria_confirm_delete.html
│   │       ├── etiquetas_list.html
│   │       ├── etiqueta_form.html
│   │       └── etiqueta_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

## Guía de Instalación y Ejecución

A continuación se detallan los pasos para instalar, configurar y ejecutar el proyecto:

### Paso 1: Preparar el entorno virtual

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

### Paso 2: Instalar las dependencias

```bash
pip install django
```

### Paso 3: Clonar o descargar el proyecto

Puedes descargar todos los archivos del proyecto o clonarlos desde un repositorio. Asegúrate de mantener la estructura de carpetas intacta.

### Paso 4: Configurar la base de datos

```bash
# Navegar al directorio del proyecto
cd gestor_tareas_django

# Realizar las migraciones
python manage.py makemigrations tasks
python manage.py migrate
```

### Paso 5: Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### Paso 6: Ejecutar la aplicación

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000/`

## Guía de Uso

### Página Principal

Al acceder a la aplicación, verás la página principal con:
- Un panel lateral con las categorías disponibles
- Un listado de tareas existentes
- Botón para crear nuevas tareas

### Gestión de Tareas

1. **Crear una tarea**:
   - Haz clic en el botón "Nueva tarea"
   - Completa el formulario con título, descripción, categoría, prioridad y fecha de vencimiento
   - Selecciona las etiquetas que desees asociar
   - Haz clic en "Guardar"

2. **Ver detalles de una tarea**:
   - Haz clic en el icono de ojo en la tarea deseada
   - Verás todos los detalles de la tarea

3. **Editar una tarea**:
   - Haz clic en el icono de lápiz en la tarea deseada
   - Modifica los campos necesarios
   - Haz clic en "Guardar cambios"

4. **Eliminar una tarea**:
   - Haz clic en el icono de papelera en la tarea deseada
   - Confirma la eliminación en la página que aparece

5. **Marcar como completada**:
   - Marca la casilla de verificación junto a la tarea
   - La tarea se mostrará como completada

### Gestión de Categorías

1. **Ver categorías**:
   - Haz clic en "Categorías" en la barra de navegación
   - Verás todas las categorías disponibles

2. **Crear una categoría**:
   - Haz clic en "Nueva categoría"
   - Completa el formulario con nombre, descripción y color
   - Haz clic en "Guardar"

3. **Ver tareas por categoría**:
   - Haz clic en una categoría en el panel lateral
   - Verás solo las tareas de esa categoría

### Gestión de Etiquetas

1. **Ver etiquetas**:
   - Haz clic en "Etiquetas" en la barra de navegación
   - Verás todas las etiquetas disponibles

2. **Crear una etiqueta**:
   - Haz clic en "Nueva etiqueta"
   - Completa el formulario con nombre y color
   - Haz clic en "Guardar"

## Personalización

El proyecto está diseñado para ser fácilmente personalizable:

- **Colores**: Modifica las variables CSS en `static/tasks/css/style.css`
- **Modelos**: Edita los modelos en `tasks/models.py`
- **Vistas**: Personaliza las vistas en `tasks/views.py`
- **Plantillas**: Modifica las plantillas en `tasks/templates/tasks/`

## Solución de Problemas

### Base de datos

Si encuentras problemas con la base de datos:
1. Elimina el archivo `db.sqlite3` si existe
2. Elimina la carpeta `tasks/migrations` (excepto `__init__.py`)
3. Ejecuta `python manage.py makemigrations tasks`
4. Ejecuta `python manage.py migrate`

### Errores de dependencias

Si encuentras errores relacionados con dependencias:
```bash
pip install -r requirements.txt
```
Si no existe el archivo requirements.txt, asegúrate de tener instalado Django:
```bash
pip install django
```

## Conclusión

Este Gestor de Tareas es una aplicación completa que demuestra el uso de Django para crear aplicaciones web funcionales y atractivas. Cumple con todos los requisitos técnicos establecidos y proporciona una experiencia de usuario intuitiva y agradable.
