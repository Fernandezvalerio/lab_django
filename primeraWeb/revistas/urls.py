
#creamos la vista y url
from django.urls import path
from . import views  # Importa tus vistas correctamente

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),  # Asegúrate de no usar include aquí
]