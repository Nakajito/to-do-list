from django.shortcuts import render

def tasks_list(request):
    task_list = [
        'Programar',
        'Leer',
        'Videojuegos',
        'Ejercicio',
        ]

    return render(request, 'tasks/tasks_list.html', {
        'title' : 'Lista de tareas',
        'header' : 'Lista de actividades',
        'task_list' : task_list,
    })