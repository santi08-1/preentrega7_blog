from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
def inicio(request):
    posts = Post.objects.filter(estado="Publicado").order_by("-fecha_creacion")
    return render(request, 'posts/inicio.html', {'posts': posts})

def acerca(request):
    return render(request, 'posts/acerca.html')

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PostForm()
        return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Crear'})

def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return render(request, 'posts/post_confirm_delete.html', {'post': post})
    return render(request, 'posts/eliminar_post.html', {'post': post})
