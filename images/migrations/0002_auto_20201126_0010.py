# Generated by Django 3.1.3 on 2020-11-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]