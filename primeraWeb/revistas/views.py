from django.shortcuts import render

# creacion de la vista para el html

from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()  # Consulta todos los libros
    return render(request, 'lista_libros.html', {'libros': libros})

from django.http import HttpResponseRedirect

def inicio(request):
    return HttpResponseRedirect('/libros/')  # Redirecciona a la URL de libros