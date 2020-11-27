from django.test import TestCase, Client

from .models import Image


class TestUploadImage(TestCase):
    """Тестирование Загрузки изображений"""
    def setUp(self):
        self.client = Client()

    def test_upload_local(self):
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
        url = 'https://lakebaikal.ru/upload/iblock/9bf/VA2-3.jpg'
        response = self.client.post('/add_image/', {'url': url})
        image = Image.objects.all()[0]
        self.assertRedirects(
            response, f'/{image.id}/',
             status_code=302, target_status_code=200)


        


