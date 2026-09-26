"""
Vistas de la aplicación library.

Toda la información se sirve desde una única URL (/):

- dashboard: listado de libros, autores, categorías y editoriales,
  con buscador en vivo y fichaampliada en modal (sin recargar).
- book_detail: redirige a la URL única conservando el ancla del libro,
  de modo que los enlaces antiguos sigan funcionando.
"""

from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from library.models import Autor, Categoria, Editorial, Libro
from library.utils import imagen_url


def _autor_dict(autor):
    """Serializa un autor junto con su perfil biográfico opcional."""

    perfil = getattr(autor, 'perfil_autor', None)

    return {
        'id': autor.pk,
        'nombre': autor.nombre,
        'apellido': autor.apellido,
        'completo': str(autor),
        'nacionalidad': autor.nacionalidad,
        'nacimiento': autor.fecha_nacimiento.isoformat(),
        'foto': imagen_url(autor.foto),
        'biografia': perfil.biografia if perfil else '',
        'lugar': perfil.lugar_nacimiento if perfil else '',
    }


def _libro_dict(libro):
    """Serializa un libro con toda la información necesaria para la ficha."""

    return {
        'id': libro.pk,
        'titulo': libro.titulo,
        'isbn': libro.isbn,
        'anio': libro.anio_publicacion,
        'paginas': libro.numero_paginas,
        'sinopsis': libro.sinopsis,
        'portada': imagen_url(libro.portada),
        'autor': _autor_dict(libro.autor),
        'categorias': [c.nombre for c in libro.categorias.all()],
        'publicaciones': [
            {
                'editorial': p.editorial.nombre,
                'pais': p.editorial.pais,
                'fecha': p.fecha.isoformat(),
                'edicion': p.edicion,
            }
            for p in libro.publicaciones.all()
        ],
    }


def dashboard(request):
    """Página única con el catálogo completo de la biblioteca."""

    libros = list(
        Libro.objects.all()
        .select_related('autor', 'autor__perfil_autor')
        .prefetch_related('categorias', 'publicaciones__editorial')
    )

    autores = list(
        Autor.objects.all()
        .select_related('perfil_autor')
        .annotate(total_libros=Count('libros'))
    )
    categorias = list(Categoria.objects.all().annotate(total=Count('libros')))
    editoriales = list(
        Editorial.objects.all().annotate(total=Count('publicaciones'))
    )

    datos = [_libro_dict(libro) for libro in libros]

    contexto = {
        'libros': libros,
        'autores': autores,
        'categorias': categorias,
        'editoriales': editoriales,
        'datos_json': datos,
        'total_paginas': sum(l.numero_paginas for l in libros),
    }

    return render(request, 'library/dashboard.html', contexto)


def book_detail(request, pk):
    """Redirige a la URL única abriendo la ficha del libro indicado."""

    get_object_or_404(Libro, pk=pk)

    return redirect(f"{reverse('library:dashboard')}#libro-{pk}")
