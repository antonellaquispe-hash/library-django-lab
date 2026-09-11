"""
Vistas de la aplicación library.
"""

from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch

from library.models import Autor, Categoria, Editorial, Libro, PerfilAutor, Publicacion


def book_detail(request, pk):
    """Vista que muestra el detalle de un libro específico."""

    libro = get_object_or_404(Libro.objects.select_related('autor'), pk=pk)

    # Datos del autor y su perfil biográfico
    autor = libro.autor
    try:
        perfil = autor.perfil_autor
    except PerfilAutor.DoesNotExist:
        perfil = None

    # Categorías del libro
    categorias = libro.categorias.all()

    # Publicaciones del libro (relaciona libro y editorial con fecha y edición)
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