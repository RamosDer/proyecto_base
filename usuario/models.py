from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.Charfield(max_length=100)
    apellido = models.Charfield(max_length=100)
    email = models.Charfield(max_length=100)
    telefono = models.Charfield(max_length=100)
    nombre_usuario = models.Charfield(max_length=100)
    roles = models.Charfield(max_length=100,default="observador")
    def __str__(self):
        return self.nombre_usuario