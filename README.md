# PNUD_py_django

## Proyecto Blog en Django (Python)
### Requisitos previos
***
* PostgreSQL (12.7 o más)
* Python 3.8 o más
* pip 23.0.1
* Django 3.2.3

**Nota:** Se recomienda que al momento de la instalación de PostgreSQL utilizar el usuario por defecto (postgres) y una contraseña fácil de recordar.
### Proceso de instalación
***
Para que el proyecto funcione correctamente se deben seguir los siguientes pasos:

**1.** Clonar el proyecto

**2.** Configurar .env: Se debe copiar el archivo .env.example y agregar la configuración de la BD, es importante usar el usuario y contraseña el cual se utilizó al momento de la instalación de PostgreSQL.

**3.** Instalar las siguientes librerías:
   * pip install psycopg2
   * pip install Pillow
   * pip install django-widget-tweaks
   * pip install django-environ
   * pip install django-environment
   * pip install djangorestframework
   * pip install docutils

**4.** Crear la Base de Datos con el nombre **news**:

**5.** Crear y ejecutar las migraciones, para esto se deben utilizar los siguientes usuarios:
   * py manage.py makemigrations
   * py manage.py migrate
   
**6.** Crear un super-usuario, ejecutar el comando:
   * py manage.py createsuperuser
   
**7.** Cargar los archivos .sql en la Base de Datos que se encuentra en la carpeta *documentos*.

## Estructura del proyecto
***
* Carpeta **blog** 
  * Contiene imágenes de prueba
* Carpeta **blog_App** 
  * Carpeta **static**
    * Archivos CSS de las vistas de base y home 
  * Carpeta **templates**
    * Carpeta **registration**
      * Vista **login.html** para iniciar sesión
      * Vista **password_change.html** para cambiar la contraseña de un usuario
      * Vista **password_change_done.html** contiene mensaje en caso de que el cambio de contraseña sea exitoso.
    * Vista base.html (Plantilla para las vistas html)
    * Vista **create_new.html** formulario para crear noticias
    * Vista **edit_new.html** formulario para editar noticias
    * Vista **home.html** se muestra como página de inicio del proyecto
    * Vista **news_table.html** se muestra al iniciar sesión con un usuario registrado, presenta una tabla para administrar las noticias.
    * Vista **newscategory.html** se muestran las noticias con filtro de acuerdo a la categoría
    * Vista **newsindex.html** se muestra al presionar "Noticias" en el menú principal, se presentan todas las noticias
    * Vista **newsitem.html** se muestra al presionar "Leer más" en las tarjetas de noticias para poder visualizar el contenido de cada noticia
    * Vista **register.html** se muestra al presionar "Registrar" en el menú principal, se usa para registrar un usuario nuevo
  * Archivo **admin.py** donde se realiza la configuración de los modelos para el admin de Django.
  * Archivo **forms.py** donde se encuentran los formularios utilizados en la aplicación.
  * Archivo **models.py** donde se encuentran los modelos que se utilizarán en la aplicación.
  * Archivo **urls.py** donde se encuentra configurado cada una de las rutas que usa la aplicación.
  * Archivo **views.py** donde se encuentra cada una de las vistas para cada una de las funcionalidades de la aplicación.
* Carpeta **blog_App** 
  * Archivo **.env.example** donde se encuentra un ejemplo del archivo .env para la respectiva configuración
  * Archivo **settings.py** donde se encuentra la configuración principal del proyecto.
  * Archivo **urls.py** donde se encuentran las rutas principales que va a utilizar la aplicación.

## Integrantes y Descripción del proyecto
***
La aplicación *blog de noticias* permite crear diferentes noticias, en las cuales un usuario puede publicar su punto de vista y algunas novedades sobre un tema de interés público.

**Integrantes:**
* Esteban Rios
* Alex Ortiz


 
                

