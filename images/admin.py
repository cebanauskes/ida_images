from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'pub_date',
        'url',
    )
    empty_value_display = '-пусто-'


admin.site.register(Image, ImageAdmin)