from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری')
    name = models.CharField(max_length=30, verbose_name='نام')
    family = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    pic = models.ImageField(upload_to='upload/profile/images', default='upload/profile/profile.png', verbose_name="تصویر")
    bio = models.TextField(max_length=500, blank=True, verbose_name='بیوگرافی')
    website = models.URLField(blank=True, verbose_name='وب سایت')
    phone = PhoneField(verbose_name="شماره تماس", blank=True)
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    def __str__(self):
        return f"{self.user}"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
