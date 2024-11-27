from django.db import models

# creacion del modelo de la revista 

from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=100, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.titulo

class Reseña(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.CharField(max_length=100)  # Nombre del usuario que deja la reseña
    texto_reseña = models.TextField()
    calificacion = models.IntegerField()  # Calificación de 1 a 5
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario} para {self.libro.titulo}"
