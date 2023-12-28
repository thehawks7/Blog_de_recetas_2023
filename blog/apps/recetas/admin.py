from django.contrib import admin
from .models import Categoria, Receta

# Register your models here.

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo','subtitulo','fecha','texto','categorias','imagenes')

admin.site.register(Categoria)