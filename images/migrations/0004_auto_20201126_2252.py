# Generated by Django 3.1.3 on 2020-11-26 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20201126_2228'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageModel',
            new_name='Image',
        ),
    ]