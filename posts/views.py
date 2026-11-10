from django.shortcuts import render
from .models import Post
# Create your views here.
def inicio(request):
    posts = Post.objects.filter(estado="Publicado").order_by("-fecha_creacion")
    return render(request, 'posts/inicio.html', {'posts': posts})

def acerca(request):
    return render(request, 'posts/acerca.html')