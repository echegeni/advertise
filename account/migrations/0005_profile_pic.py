# Generated by Django 3.1.5 on 2021-01-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210111_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='upload/images/no-img.jpg', upload_to='upload/product/images', verbose_name='تصویر'),
        ),
    ]