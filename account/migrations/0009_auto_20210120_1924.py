# Generated by Django 3.1.5 on 2021-01-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_profile_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='upload/profile/profile.png', upload_to='upload/profile/images', verbose_name='تصویر'),
        ),
    ]