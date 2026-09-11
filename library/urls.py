"""
URLs de la aplicación library.
"""

from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('<int:pk>/', views.book_detail, name='detail'),
]