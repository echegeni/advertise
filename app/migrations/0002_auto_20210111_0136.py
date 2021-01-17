# Generated by Django 3.1.5 on 2021-01-10 22:06

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهر ها'},
        ),
        migrations.AlterField(
            model_name='advertise',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, verbose_name='شماره تماس'),
        ),
    ]
