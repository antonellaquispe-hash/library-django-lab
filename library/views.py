"""
Vistas de la aplicación library.

Proporciona:
- book_list: lista de todos los libros con portada y enlace al detalle.
- book_detail: detalle de un libro específico.
"""

from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch

from library.models import Autor, Categoria, Editorial, Libro, PerfilAutor, Publicacion


def book_list(request):
    """Vista que muestra una lista visual de todos los libros registrados."""

    libros = Libro.objects.all().select_related('autor')

    return render(request, 'library/book_list.html', {'libros': libros})


def book_detail(request, pk):
    """Vista que muestra el detalle de un libro específico."""

    libro = get_object_or_404(Libro.objects.select_related('autor'), pk=pk)

    autor = libro.autor

    try:
        perfil = autor.perfil_autor
    except PerfilAutor.DoesNotExist:
        perfil = None

    categorias = libro.categorias.all()

    publicaciones = (
        Publicacion.objects.filter(libro=libro)
        .select_related('editorial')
        .order_by('fecha')
    )

    return render(request, 'library/book_detail.html', {
        'libro': libro,
        'autor': autor,
        'perfil': perfil,
        'categorias': categorias,
        'publicaciones': publicaciones,
    })