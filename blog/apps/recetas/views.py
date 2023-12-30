from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Post, Categoria, Receta, Comentario, Usuario
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required   
from django.http import Http404, HttpResponse, HttpResponseForbidden
from .forms import PostForm, ComentarioForm

# Create your views here.
def DetalleReceta(request, pk):


    n = Receta.objects.get(pk = pk) # SELECT * FROM NOTICIAS WHERE id = 1
    c = n.comentarios.all()


    #BORRAR NOTICIA
    if request.method == 'POST' and 'delete_receta' in request.POST:
        n.delete()
        return redirect('recetas:listar')
   
    #COMENTARIO
    if request.method == 'POST' and 'add_comentario' in request.POST:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            form.save()
            return redirect('recetas:detalle', pk=pk)
    else:
        form = ComentarioForm()
   
    contexto = {
        'recetas': n,
        'comentarios': c,
        'form': form,
    }


    return render (request, 'recetas/detalle.html', contexto)


def ListarRecetas(request):
    contexto = {}
    id_categoria = request.GET.get("id", None)


    if id_categoria:
        n = Receta.objects.filter(categorias = id_categoria)
    else:
        n = Receta.objects.all() # SELECT * FROM NOTICIAS
    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['recetas'] = n
    contexto['categorias'] = cat

        # filtrar por antiguedad asc
    antiguedad_asc = request.GET.get("antiguedad_asc")
    if antiguedad_asc:
        n = Receta.objects.all().order_by('fecha') #ordena por fecha


    # filtrar por antiguedad desc
    antiguedad_desc = request.GET.get("antiguedad_desc")
    if antiguedad_desc:
        n = Receta.objects.all().order_by('-fecha') #ordena por fecha


    # filtrar por orden alfabetico asc
    orden_asc = request.GET.get("orden_asc")
    if orden_asc:
        n = Receta.objects.all().order_by('titulo') #ordena por titulo


    # filtrar por orden alfabetico desc
    orden_desc = request.GET.get("orden_desc")
    if orden_desc:
        n = Receta.objects.all().order_by('-titulo') #ordena por titulo



    return render (request, 'recetas/listar.html', contexto)


@login_required
def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES) ##Request files es para las imagenes


        if form.is_valid():
            recetas = form.save(commit=False)
            recetas.autor = request.user
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render (request, 'recetas/addpost.html', {'form':form})



@login_required
def AddComentario(request, receta_id):


    receta = get_object_or_404(Receta, id = receta_id)  
    if request.method == 'POST':
        contenido = request.POST.get("contenido")
        usuario = request.user.username
        # creacion de comentario
        Comentario.objects.create(receta = receta, usuario = usuario, contenido = contenido)
   
    return redirect('recetas:detalle', pk = receta_id)


@login_required
def BorrarComentario(request, comentario_id):


    comentario = get_object_or_404(Comentario, id = comentario_id)  
    if comentario.usuario == request.user.username:
        comentario.delete()
   
    return redirect('recetas:detalle', pk = comentario.receta.pk)


@login_required
def EditarReceta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)


    # Solo el autor puede editar la noticia
    if receta.autor != request.user:
        return HttpResponseForbidden("No tenes permiso para editar esta receta.")


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('recetas:detalle', pk=pk)
    else:
        form = PostForm(instance=receta)


    context = {
        'form': form,
    }
    return render(request, 'noticias/editar.html', context)


# EDITAR COMENTARIOS
@login_required #debes estar loggeado para poder editar
def EditarComentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)


    # mensaje de error si no sos el autor del comentario
    if comentario.usuario != request.user.username:
        messages.error(request, 'No tenes permiso para editar este comentario')
        return redirect('recetas:detalle', pk=comentario.receta.pk)
   
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('recetas:detalle', pk=comentario.receta.pk)
    else:
        form = ComentarioForm(instance=comentario)
   
    contexto = {
        'form':form,
        'comentario':comentario,
    }


    return render(request, 'recetas/editar_comentario.html', contexto)
