from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Image
from .forms import ImageForm, ResizeForm
from .utils import resize


def index(request):
    """Главная страница"""
    image_list = Image.objects.all()
    return render(request, 'index.html', {'image_list': image_list})

def add_image(request):
    """Страница добавления нового изображения"""
    if request.method == 'POST':
        form = ImageForm(request.POST or None, files=request.FILES or None)

        if form.is_valid():
            image = form.save()
            return redirect('image_detail', image_id=image.id)
        
    else:
        form = ImageForm()
    return render(request, 'imageNew.html', {'form': form,})

def image_detail(request, image_id):
    """Страница изображения с возможностью изменения его размера.
    Параметры Height и Width прописываются относительно 
    изначально загруженного изображения
    
    """
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        form = ResizeForm(request.POST or None)

        if form.is_valid():
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            resize(image, height, width)
            return redirect('image_detail', image_id=image.id)
    
    else:
        form = ResizeForm()
    return render(request, 'imageDetail.html', {'image': image, 'form': form, })







