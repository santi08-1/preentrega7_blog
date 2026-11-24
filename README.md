# Pre-entrega 10: CRUD y Manejo de Imágenes

Se implementó el flujo completo de creación, lectura, edición y eliminación de publicaciones (crud), junto con la carga de imágenes:

 **Procesamiento de imágenes:** Se instaló `Pillow` y se agregaron al archivo `requirements.txt`.
**Configuración de archivos multimedia:** En `settings.py` se definieron `MEDIA_URL` y `MEDIA_ROOT`, y en `urls.py` se habilitó el servicio de archivos multimedia en modo desarrollo (`DEBUG = True`).
**Modelo y formulario:** Se incorporó el campo `ImageField` al modelo `Post` y se creó `PostForm` (`ModelForm`) para gestionar los campos del formulario.
**Formularios y vistas CRUD:** Se configuró `enctype="multipart/form-data"` en los formularios con carga de archivos y se implementaron las vistas y URLs para crear, ver detalle, editar y borrar publicaciones.