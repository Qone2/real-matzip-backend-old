# Generated by Django 3.2 on 2021-05-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matzip', '0003_auto_20210502_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='matzip',
            name='image',
            field=models.ImageField(default='media/kkobookchip.png', upload_to=''),
        ),
    ]
