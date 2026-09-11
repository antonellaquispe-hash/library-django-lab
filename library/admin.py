from django.contrib import admin

from .models import Autor, Categoria, Editorial, Libro, PerfilAutor, Publicacion


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    """Configuración del modelo Autor en el administrador."""

    list_display = ('nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido', 'nacionalidad')


@admin.register(PerfilAutor)
class PerfilAutorAdmin(admin.ModelAdmin):
    """Configuración del modelo PerfilAutor en el administrador."""

    list_display = ('autor', 'lugar_nacimiento')
    search_fields = ('autor__nombre', 'autor__apellido')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    """Configuración del modelo Libro en el administrador."""

    list_display = (
        'titulo',
        'autor',
        'isbn',
        'anio_publicacion',
        'numero_paginas',
    )
    search_fields = ('titulo', 'isbn', 'autor__nombre', 'autor__apellido')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuración del modelo Categoria en el administrador."""

    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    """Configuración del modelo Editorial en el administrador."""

    list_display = ('nombre', 'pais', 'direccion', 'email')
    search_fields = ('nombre', 'pais')


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    """Configuración del modelo Publicacion en el administrador."""

    list_display = ('libro', 'editorial', 'fecha', 'edicion')
    search_fields = ('libro__titulo', 'editorial__nombre')