from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido= models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='publicado')

    def __str__(self):
        return self.titulo

