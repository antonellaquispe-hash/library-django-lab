"""
URLs de la aplicación library.

La biblioteca se muestra completa en una única URL:

- /                      → catálogo completo (libros, autores, categorías, editoriales)
- /<int:pk>/             → redirige a /#libro-<pk> para conservar los enlaces antiguos
"""

app_name = 'library'

from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.book_detail, name='detail'),
]
