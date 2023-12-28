from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def nosotros(request):
    return render(request, 'nosotros.html')
def recetas(request):
    return render(request, recetas.html)
def base(request):
    return base(request, base.html)
def addPost(request):
    return base(request, addPost.html)