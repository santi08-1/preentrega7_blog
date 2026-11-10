from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'estado')
    list_filter = ('estado', 'autor')
    search_fields = ('titulo', 'contenido')

admin.site.register(Post, PostAdmin)