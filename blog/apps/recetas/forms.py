from django import forms
from .models import Receta, Comentario


class PostForm(forms.ModelForm):


    class Meta:
        model = Receta
        fields = [
            'titulo',
            'resumen',
            'texto',
            'imagenes',
            'categorias',
        ]


class ComentarioForm(forms.ModelForm):
   
    class Meta:
        model = Comentario
        fields = [
            'contenido',
        ]
        exclude = ['usuario']
   
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)


        super(ComentarioForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario = user.username


