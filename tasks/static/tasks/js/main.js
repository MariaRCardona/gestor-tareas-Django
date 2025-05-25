// Funcionalidad para el gestor de tareas
document.addEventListener('DOMContentLoaded', function() {
    // Mostrar/ocultar modal
    const modalToggles = document.querySelectorAll('[data-toggle="modal"]');
    const modalBackdrops = document.querySelectorAll('.modal-backdrop');
    const modalCloses = document.querySelectorAll('.modal-close');
    
    modalToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetModal = document.querySelector(targetId);
            if (targetModal) {
                targetModal.classList.add('show');
            }
        });
    });
    
    modalCloses.forEach(close => {
        close.addEventListener('click', function() {
            const modal = this.closest('.modal-backdrop');
            if (modal) {
                modal.classList.remove('show');
            }
        });
    });
    
    modalBackdrops.forEach(backdrop => {
        backdrop.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('show');
            }
        });
    });
    
    // Marcar tarea como completada
    const taskCheckboxes = document.querySelectorAll('.task-checkbox');
    
    taskCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskItem = this.closest('.task-item');
            if (this.checked) {
                taskItem.classList.add('completed');
                showToast('¡Tarea completada!', 'success');
            } else {
                taskItem.classList.remove('completed');
            }
            
            // Aquí se enviaría una petición AJAX para actualizar el estado en la base de datos
            const taskId = taskItem.getAttribute('data-id');
            const completed = this.checked;
            
            // Usar CSRF token para peticiones POST en Django
            const csrftoken = getCookie('csrftoken');
            
            fetch(`/tasks/completar/${taskId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({
                    completada: completed
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log(`Tarea ${taskId} marcada como ${completed ? 'completada' : 'pendiente'}`);
                } else {
                    console.error('Error al actualizar la tarea');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
    
    // Filtrar por categoría
    const categoryItems = document.querySelectorAll('.category-item');
    
    categoryItems.forEach(item => {
        item.addEventListener('click', function() {
            // Eliminar clase active de todos los items
            categoryItems.forEach(cat => cat.classList.remove('active'));
            
            // Añadir clase active al item seleccionado
            this.classList.add('active');
            
            const categoryId = this.getAttribute('data-id');
            const categoryName = this.querySelector('.category-name').textContent.trim();
            
            // Actualizar título del contenido
            const contentTitle = document.querySelector('.content-title');
            if (contentTitle) {
                contentTitle.textContent = categoryName || 'Todas las tareas';
            }
            
            // Redirigir a la página de la categoría o todas las tareas
            if (categoryId === 'all') {
                window.location.href = '/tasks/';
            } else {
                window.location.href = `/tasks/categoria/${categoryId}/`;
            }
        });
    });
    
    // Función para mostrar notificaciones toast
    function showToast(message, type = 'info') {
        const toastContainer = document.querySelector('.toast-container') || createToastContainer();
        
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        
        let icon = '';
        switch(type) {
            case 'success':
                icon = '<i class="fas fa-check-circle"></i>';
                break;
            case 'error':
                icon = '<i class="fas fa-exclamation-circle"></i>';
                break;
            case 'warning':
                icon = '<i class="fas fa-exclamation-triangle"></i>';
                break;
            default:
                icon = '<i class="fas fa-info-circle"></i>';
        }
        
        toast.innerHTML = `${icon}${message}`;
        toastContainer.appendChild(toast);
        
        // Eliminar el toast después de 3 segundos
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
    
    function createToastContainer() {
        const container = document.createElement('div');
        container.className = 'toast-container';
        document.body.appendChild(container);
        return container;
    }
    
    // Función para obtener el CSRF token de las cookies (necesario para Django)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // Validación de formularios
    const taskForm = document.getElementById('taskForm');
    
    if (taskForm) {
        taskForm.addEventListener('submit', function(e) {
            const title = document.getElementById('id_titulo').value.trim();
            const category = document.getElementById('id_categoria').value;
            
            if (!title) {
                e.preventDefault();
                showToast('Por favor, ingresa un título para la tarea', 'error');
                return;
            }
            
            if (!category) {
                e.preventDefault();
                showToast('Por favor, selecciona una categoría', 'error');
                return;
            }
        });
    }
});
