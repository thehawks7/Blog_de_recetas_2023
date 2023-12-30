from django.urls import path
from . import views


app_name = 'recetas'


urlpatterns = [
    path('', views.ListarRecetas, name='listar'),
    path('detalle/<int:pk>', views.DetalleReceta, name='detalle'),
    path('addpost', views.AddPost, name='addpost'),
    path('comentario/delete/<int:comentario_id>', views.BorrarComentario, name='delete_comentario'),
    path('recetas/<int:pk>/edit/', views.EditarReceta, name='edit_receta'),
    path('comentario/edit/<int:comentario_id>', views.EditarComentario, name='edit_comentario'),


]
