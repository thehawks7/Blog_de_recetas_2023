from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuario

# Create your models here.




#CATEGORIA
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoría')
    imagenes = models.ImageField(null=True, blank=True, upload_to='recetas', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
        
    def delete(self, using =None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()
            


class Receta(models.Model):
    titulo = models.CharField(max_length=50) # = VARCHAR | max_length longitud max
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    resumen = models.CharField(max_length=200, null=True)
    texto = models.TextField()
    #imagen requiere la libreria pillow
    imagenes = models.ImageField(null=True, blank=True, upload_to='recetas', default='static/post_default.png')
    fecha = models.DateTimeField(auto_now_add=True)
    categorias = models.ForeignKey(Categoria, on_delete= models.SET_NULL, null=True) # models.CASCADE
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=Usuario.objects.get(is_superuser=True).pk)


    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    noticia = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=50)


    def __str__(self):
        return self.contenido