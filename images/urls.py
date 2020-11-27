from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_image/', views.add_image, name='add_image'),
    path('<int:image_id>/', views.image_detail, name='image_detail')
]