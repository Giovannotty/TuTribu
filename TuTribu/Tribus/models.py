from django.db import models
from django.db.models import base

# Create your models here.
#class customer(models.Model):
    #pass

class Tribe(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(null=True, blank=True) 

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nuevo_Evento = models.CharField(max_length=100)
    definir_Evento = models.CharField(max_length=200)
    fecha_Evento = models.DateField()
    horas_evento= models.TimeField(null=True, blank=True)
    costo = models.FloatField(default=0)
    añadir_comentarios = models.TextField(max_length=200)
    localizacion_Evento = models.CharField(max_length=200)
    imagen_Evento = models.ImageField(null=True, blank=True)
    archivoInfo = models.FileField(null=True, blank=True)


    def agregar_Comentario(self):
        pass

    def actualizar_Comentario(self):
        pass

    def eliminar_Comentario(self):
        pass


class Post(models.Model):
    postId = models.CharField(max_length=40)
    post_fecha_pub = models.DateField(auto_now_add=True)
    postTitulo = models.TextField()
    postDescripcion = models.TextField()
    postImagen = models.ImageField(null=True, blank=True)
    #postTribu = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.postTribu.nombre

class Reaccion(models.Model):
    Accion = models.CharField(max_length=200)
    Imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Accion

class ReaccionPost(models.Model):
    #Reacc = models.Foreignkey(Reaccion, on delette=models.SET_NULL, null=True)
    #Posted = models.Foreignkey(Post, on delette=models.CASCADE)
    NumReact = models.IntegerField(default=0)

    def __str__(self):
        return self.Accion

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    idPost = models.IntegerField(default=0)
    fecha = models.DateField(auto_now_add=True)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contenido = models.TextField()

    def agregar_Evento(self):
        pass

    def actualizar_Evento(self):
        pass

    def eliminar_Evento(self):
        pass



