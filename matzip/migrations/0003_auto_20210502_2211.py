# Generated by Django 3.2 on 2021-05-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matzip', '0002_auto_20210502_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matzip',
            old_name='url_320',
            new_name='img_url',
        ),
        migrations.RemoveField(
            model_name='matzip',
            name='url',
        ),
        migrations.AddField(
            model_name='matzip',
            name='post_url',
            field=models.CharField(default=None, max_length=200),
        ),
    ]