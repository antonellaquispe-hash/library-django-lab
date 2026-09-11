from django.db import models


class Autor(models.Model):
    """Representa a la persona que escribe los libros."""

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class PerfilAutor(models.Model):
    """Guarda los datos biográficos adicionales de un autor."""

    autor = models.OneToOneField(
        Autor,
        on_delete=models.CASCADE,
        related_name='perfil_autor',
        verbose_name='Autor',
    )
    biografia = models.TextField()
    lugar_nacimiento = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Perfil de autor'
        verbose_name_plural = 'Perfiles de autores'
        ordering = ['autor']

    def __str__(self):
        return f'Perfil de {self.autor}'


class Libro(models.Model):
    """Representa un libro disponible en la biblioteca."""

    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    anio_publicacion = models.PositiveIntegerField()
    numero_paginas = models.PositiveIntegerField()
    sinopsis = models.TextField(blank=True)
    portada = models.ImageField(upload_to='libros/', blank=True, null=True)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        related_name='libros',
        verbose_name='Autor',
    )
    categorias = models.ManyToManyField(
        'Categoria',
        related_name='libros',
        verbose_name='Categorías',
    )
    editoriales = models.ManyToManyField(
        'Editorial',
        through='Publicacion',
        related_name='libros',
        verbose_name='Editoriales',
    )

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Editorial(models.Model):
    """Representa la empresa que publica los libros."""

    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    logo = models.ImageField(upload_to='editoriales/', blank=True, null=True)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    """Representa la publicación de un libro por una editorial."""

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='publicaciones',
        verbose_name='Libro',
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name='publicaciones',
        verbose_name='Editorial',
    )
    fecha = models.DateField()
    edicion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['fecha', 'libro']

    def __str__(self):
        return f'{self.libro} - {self.editorial} ({self.fecha})'


class Categoria(models.Model):
    """Representa la clasificación temática de los libros."""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre