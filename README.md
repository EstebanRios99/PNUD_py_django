# PNUD_py_django

DJANGO / PYTHON
1. Ejecución

   - Pasos para instalar 
    
     - Instalar Postgres

        1.1 Clonar el proyecto

        1.2 Configurar .env

    2. Ejecutar los siguientes comandos:

        Los comamndos se deben ejecutar en el directorio donde se clonó el proyecto    

        2.1 pip install django-widget-tweaks

        2.2 pip install psycopg2

        2.3 python -m pip install Pillow

        2.4 pip install django-environ

        2.5 pip install djangorestframework

    3. Crear la migración de Base de Datos:

        3.1 py manage.py makemigrations

        3.2 py manage.py migrate


2. Estructura

    2.1 Carpeta blog con imágenes de prueba

    2.2 Carpeta blog_App 

        2.2.1 Carpeta static

                Archivos CSS de las vistas de base y home 

        2.2.2 Carpeta templates

               Carpeta registration y la vista login.html para iniciar sesión 

               Vista base.html (Plantilla para las vistas html)

               Vista create_new.html formulario para crear noticias

               Vista edit_new.html formulario para editar noticias

               Vista home.html se muestra como página de inicio del proyecto

               Vista newscategory.html se muestran las noticias con filtro de acuerdo a la categoría

               Vista newsindex.html se muestra al presionar "Noticias" en el menú principal, se presentan todas las noticias

               Vista newsitem.html se muestra al presionar "Leer más" en las tarjetas de noticias para poder visualizar el contenido de cada noticia

               Vista register.html se muestra al presionar "Registrar" en el menú principal, se usa para registrar un usuario nuevo


Miembros

Esteban Ríos

Alex Ortiz


La aplicación blog de noticias permite crear diferentes noticias, en las cuales un usuario puede publicar su punto de vista y algunas novedades sobre un tema de interés público 
                

