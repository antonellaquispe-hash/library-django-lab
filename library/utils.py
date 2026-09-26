"""Utilidades compartidas por la aplicación library."""

from pathlib import Path

from django.conf import settings


def imagen_url(campo):
    """Devuelve la URL pública de un ImageField, o None si no hay archivo.

    Algunos registros guardan el nombre con el prefijo 'media/' duplicado,
    lo que produciría una ruta servida inexistente (/media/media/...);
    en ese caso se busca el archivo sin el prefijo.
    """

    if not campo:
        return None

    nombre = campo.name

    if not (Path(settings.MEDIA_ROOT) / nombre).exists():
        limpio = nombre.removeprefix('media/')
        if (Path(settings.MEDIA_ROOT) / limpio).exists():
            nombre = limpio
        else:
            return None

    return f'{settings.MEDIA_URL}{nombre}'
