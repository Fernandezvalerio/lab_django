from django.shortcuts import render

# creacion de la vista para el html

from django.shortcuts import render

def lista_libros(request):
    return render(request, 'lista_libros.html')  # Renderiza la plantilla desde templates
