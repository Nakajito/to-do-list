from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        'title' : 'Lista de tareas',
        'header' : 'Este es un ptoyecto para portafolio'
    })