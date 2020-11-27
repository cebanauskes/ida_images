from django.test import TestCase, Client

from .models import Image


class TestUploadImage(TestCase):
    """Тестирование Загрузки изображений"""
    def setUp(self):
        self.client = Client()


    def test_upload_local(self):
        """Тест загрузки из локального хранилища"""
        with open('test_image.jpg', 'rb') as fp:
            self.client.post('/add_image/', {'image': fp})
            image = Image.objects.all()[0]

            response = self.client.get(f'/{image.id}/')
            self.assertContains(
                    response, f'<img src="{image.image.url}"', 
                    status_code=200)
            
            response = self.client.get('/')
            self.assertContains(
                response, f'<a href="/{image.id}/"',
                status_code=200)

    def test_upload_url(self):
        """Тест загрузки по ссылке"""
        url = 'https://lakebaikal.ru/upload/iblock/9bf/VA2-3.jpg'
        self.client.post('/add_image/', {'url': url})
        image = Image.objects.all()[0]

        response = self.client.get(f'/{image.id}/')
        self.assertContains(
                response, f'<img src="{image.image.url}"', 
                status_code=200, )
        
        response = self.client.get('/')
        self.assertContains(
            response, f'<a href="/{image.id}/"',
            status_code=200)    

    def test_redirect(self):
        """Тест перенаправления пользователя на страницу 
        изображения после его загрузки
        """
        url = 'https://lakebaikal.ru/upload/iblock/9bf/VA2-3.jpg'
        response = self.client.post('/add_image/', {'url': url})
        image = Image.objects.all()[0]

        self.assertRedirects(
            response, f'/{image.id}/',
             status_code=302, target_status_code=200, )


class TestImageResize(TestCase):
    """Тестирование изменения размера изобржения"""

    def setUp(self):
        self.client = Client()
        with open('test_image.jpg', 'rb') as fp:
            self.client.post('/add_image/', {'image': fp})
        self.image = Image.objects.all()[0]
        self.height = 300
        self.width = 300

    def test_resize_height(self):
        """Тест изменения высоты изображения"""
        self.client.post(
            f'/{self.image.id}/', {'height': self.height})
        new_img = Image.objects.get(id=self.image.id)

        response = self.client.get(f'/{self.image.id}/')
        self.assertContains(
                response, f'<img src="{new_img.resized_image.url}"', 
                status_code=200)
        self.assertEqual(new_img.resized_image.height, self.height)

    def test_resize_width(self):
        """Тест изменения ширины изображения"""
        self.client.post(
            f'/{self.image.id}/', {'width': self.width})
        new_img = Image.objects.get(id=self.image.id)

        response = self.client.get(f'/{self.image.id}/')
        self.assertContains(
                response, f'<img src="{new_img.resized_image.url}"', 
                status_code=200)
        self.assertEqual(new_img.resized_image.width, self.width)

    def test_resize_form(self):
        """Тест валидации формы"""
        response = self.client.post(
            f'/{self.image.id}/',
            {'width': 0, 'height': 0})
        self.assertFormError(response, 'form', None, 'Заполните хотя бы одно поле')



        


