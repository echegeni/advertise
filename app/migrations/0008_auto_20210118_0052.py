# Generated by Django 3.1.5 on 2021-01-17 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210118_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='fav',
            field=models.BooleanField(blank=True, default=False, verbose_name='محبوب'),
        ),
        migrations.AddField(
            model_name='city',
            name='fav',
            field=models.BooleanField(blank=True, default=False, verbose_name='محبوب'),
        ),
    ]
