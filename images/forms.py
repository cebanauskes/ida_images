import requests
from urllib.request import urlopen
from urllib.error import HTTPError

from django import forms
from django.core.exceptions import ValidationError
from .models import Image
from .utils import valid_url_mimetype


class ImageForm(forms.ModelForm):
    """Форма для добавления иизображения на основе модели Image"""
    class Meta:
        model = Image
        fields = ('url', 'image',)

    def clean(self):
        """Проверяет, чтобы только одно поле было заполнено"""
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        image = cleaned_data.get('image')

        if (url and image) or (not url and not image):
            raise ValidationError(
        'Только одно поле должно быть заполнено '
        'Либо проверьте правильность введенной ссылки')

        return cleaned_data

    def clean_url(self):
        """Проверяет, работоспособна ли ссылка и
        работоспособна ли ссылка
        """
        url = self.cleaned_data.get('url')

        if url == None or url == '':
            return url

        response = requests.get(url)
        if response.status_code != 200:
            raise ValidationError('Ссылка не работает, попробуйте другую')

        if not valid_url_mimetype(url):
            raise ValidationError('Неправильное расширение файла (ожидается изображение)',)
        
        return url


class ResizeForm(forms.Form):
    """Форма для изменения размера изображения"""
    width = forms.IntegerField(
        max_value=10000, min_value=1, label='Ширина', required=False)
    height = forms.IntegerField(
        max_value=10000, min_value=1, label='Высота', required=False)

    def clean(self):
        """Проверяет, чтобы хотя бы одно поле было заполнено"""
        cleaned_data = self.cleaned_data
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')

        if width is None and height is None:
            raise ValidationError('Заполните хотя бы одно поле')
        
        return cleaned_data








        
