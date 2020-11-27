from io import BytesIO
import mimetypes
import os

from django.core.files.base import ContentFile
from PIL import Image

def resize(obj, height=None, width=None):
    """Изменение размера изображения и 
    запись нового изобржения в поле resized_image.
    
    """
    img = Image.open(obj.image).copy()
    thumb_io = BytesIO()

    if height is None:
        height = img.height

    elif width is None:
        width = img.width

    size = (width, height)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(thumb_io, format='JPEG', quality=100)
    obj.resized_image.save(
        obj.get_name, ContentFile(thumb_io.getvalue()), save=False)
    obj.save()

def valid_url_mimetype(url, mimetype_list=['image',]):
    """Проверка что при переходе по ссылке есть изображение"""
    mimetype, _ = mimetypes.guess_type(url)
    if mimetype:
        return any([mimetype.startswith(x) for x in mimetype_list])
    else:
        return False
