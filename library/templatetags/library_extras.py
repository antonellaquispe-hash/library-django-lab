"""Filtros de plantilla propios de la aplicación library."""

from django import template

from library.utils import imagen_url

register = template.Library()


@register.filter
def media_url(campo):
    """URL segura de un ImageField: '' si el archivo no existe."""

    return imagen_url(campo) or ''
