"""
URLs de la aplicación library.

- /                      → lista de libros (book_list)
- /<int:pk>/             → detalle de un libro (book_detail)
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='list'),
    path('<int:pk>/', views.book_detail, name='detail'),
]