# Generated by Django 3.1.5 on 2021-01-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_advertise_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='video',
            field=models.FileField(blank=True, upload_to='upload/product/video', verbose_name='ویدئو'),
        ),
    ]