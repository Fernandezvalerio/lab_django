
#creamos la vista y url
from django.contrib import admin
from django.urls import path, include
from revistas import views  # Importa las vistas de la app revistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Configura la raíz para redirigir a /libros/
    path('libros/', include('revistas.urls')),
]
