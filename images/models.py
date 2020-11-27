import os
from urllib.request import urlretrieve

from django.db import models
from django.core.files import File



class Image(models.Model):
    """Модель Изображения

    pub_date - поле с датой публикации изображения
    url - поле с ссылкой на изображение, если оно загружено со стороннего ресурса
    image -  поле с изображением оригинального размера
    resized_image - поле с измененным изображением

    """
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    url = models.URLField('Ссылка', blank=True, null=True)
    image = models.ImageField(upload_to='images/',
                                 blank=True, null=True)
    resized_image = models.ImageField(upload_to='resized_images/',
                                         blank=True, null=True)

    def get_remote_image(self):
        """Метод для загрузки изображения через url"""
        if self.url and not self.image:
            response = urlretrieve(self.url)
            self.image.save(os.path.basename(self.url), 
                                File(open(response[0], 'rb')))
            self.save()

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)

    @property
    def get_name(self):
        """Метод получения имени файла"""
        return os.path.basename(self.image.url)


    class Meta:
        ordering = ('-pub_date',)