# Generated by Django 3.1.5 on 2021-01-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='slug',
            field=models.SlugField(blank=True, max_length=30, verbose_name='آدرس'),
        ),
    ]