# Generated by Django 3.2 on 2021-05-21 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matzip', '0004_matzip_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matzip',
            name='image',
        ),
    ]