from django.db import models
from django.db.models import base

# Create your models here.
#class customer(models.Model):
    #pass

class Tribus(models.Model):
    pass

class Eventos(Tribus):
    nuevo_Evento = models.CharField(max_length=100)
    definir_Evento = models.CharField(max_length=200)
    fecha_Evento = models.DateField()
    horas_evento= models.TimeField(null=True, blank=True)
    costo = models.FloatField(default=0)
    añadir_comentarios = models.TextField(max_length=200)
    localizacion_Evento = models.CharField(max_length=200)
    imagen_Evento = models.ImageField(null=True, blank=True)
    archivoInfo = models.FileField(null=True, blank=True)

    def agregar_Evento(self):
        pass

    def actualizar_Evento(self):
        pass

    def eliminar_Evento(self):
        pass

    

    


class Post():
    pass
