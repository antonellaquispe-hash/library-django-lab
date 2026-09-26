Laboratorio 04 - Relación de Modelos en Django
Datos del estudiante

Nombre: Antonella Quispe
Curso: Desarrollo de Aplicaciones Empresariales
Laboratorio: 04 - Relación de Modelos en Django

Descripción

Este proyecto implementa un sistema de biblioteca utilizando Django, donde se aplican diferentes tipos de relaciones entre modelos para organizar la información de autores, libros, categorías y editoriales.

El desarrollo permite comprobar las relaciones ForeignKey, OneToOneField y ManyToManyField, además de utilizar un modelo intermedio para almacenar información adicional en la relación entre libros y editoriales.

Modelos implementados

El proyecto cuenta con los siguientes modelos:

Author: almacena la información principal de los autores.
AuthorProfile: almacena información adicional del perfil de cada autor.
Book: representa los libros registrados.
Category: representa las categorías de los libros.
Publisher: representa las editoriales.
Publication: modelo intermedio que relaciona los libros con las editoriales y almacena información adicional.
Relaciones entre modelos
Author - Book

Un autor puede tener varios libros y cada libro pertenece a un autor.

Author 1 ───────── N Book

Esta relación se implementa mediante ForeignKey.

En Book.author se utiliza:

on_delete=models.PROTECT

Esto evita que un autor pueda ser eliminado mientras tenga libros relacionados.

Author - AuthorProfile

Cada autor tiene un único perfil con información adicional.

Author 1 ───────── 1 AuthorProfile

Esta relación se implementa mediante OneToOneField.

Book - Category

Un libro puede pertenecer a varias categorías y una categoría puede estar asociada a varios libros.

Book N ───────── M Category

Esta relación se implementa mediante ManyToManyField.

Book - Publisher

La relación entre libros y editoriales utiliza el modelo intermedio Publication.

Book N ───── Publication ───── N Publisher

El modelo Publication permite almacenar información propia de la relación:

Fecha de publicación.
Edición.
Esquema de relaciones
                    ┌─────────────────┐
                    │     AUTHOR      │
                    └────────┬────────┘
                             │
                         1 : N
                             │
                             ▼
                    ┌─────────────────┐
                    │      BOOK       │
                    └───────┬─────────┘
                            │
                  ┌─────────┴──────────┐
                  │                    │
                 N:M                  N:M
                  │                    │
                  ▼                    ▼
          ┌──────────────┐     ┌────────────────┐
          │   CATEGORY   │     │  PUBLICATION   │
          └──────────────┘     └───────┬────────┘
                                       │
                                       ▼
                                ┌──────────────┐
                                │  PUBLISHER   │
                                └──────────────┘

                    ┌─────────────────┐
                    │     AUTHOR      │
                    └────────┬────────┘
                             │
                           1 : 1
                             │
                             ▼
                    ┌─────────────────┐
                    │ AUTHOR PROFILE  │
                    └─────────────────┘
Modelo intermedio: Publication

Publication permite representar la relación entre un libro y una editorial agregando información propia de dicha relación.

Los datos almacenados son:

- Libro
- Editorial
- Fecha de publicación
- Edición

De esta manera, la relación entre Book y Publisher no se limita únicamente a establecer una conexión, sino que también permite registrar información adicional.

Consultas realizadas

Se realizaron consultas en la consola de Django para comprobar las relaciones en ambos sentidos.

Consulta de ida

Se consulta el autor directamente desde un libro:

book.author
Consulta de vuelta

Se consultan los libros asociados a un autor utilizando el related_name correspondiente:

author.books.all()
Consulta mediante doble guion bajo

Se utiliza el operador __ para realizar filtros utilizando campos de modelos relacionados.

Ejemplo:

Book.objects.filter(author__name__icontains="nombre")

El nombre exacto del campo utilizado debe corresponder al definido en el modelo Author.

Comprobación de on_delete

Se comprobó el comportamiento de on_delete al intentar eliminar un autor que tiene libros relacionados.

PROTECT

El modelo Book utiliza:

on_delete=models.PROTECT

Cuando se intenta eliminar un autor que tiene libros relacionados, Django impide la eliminación y genera una excepción ProtectedError.

Esto permite proteger los libros relacionados y evitar la eliminación accidental de información.

Migraciones

Para generar y aplicar las migraciones se utilizaron los siguientes comandos:

python manage.py makemigrations
python manage.py migrate

Para comprobar el estado de las migraciones:

python manage.py showmigrations
Datos de prueba

Para comprobar el funcionamiento de las relaciones se registraron datos de prueba mediante el administrador de Django.

Se trabajó con:

2 autores.
4 libros.
3 categorías.
2 editoriales.
Publicaciones con fecha y edición.
Libros asociados a categorías.
Vista de detalle

La aplicación cuenta con una vista de detalle de un libro donde se muestran los datos relacionados.

La vista permite visualizar:

Información del libro.
Datos del autor.
Perfil del autor.
Categorías.
Editorial.
Fecha de publicación.
Edición.

Esto permite comprobar que las relaciones definidas en los modelos llegan correctamente hasta la vista y la plantilla.
