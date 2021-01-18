# Generated by Django 3.1.5 on 2021-01-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210118_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/city/', verbose_name='تصویر شهر'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/cat/', verbose_name='تصویر دسته'),
        ),
    ]