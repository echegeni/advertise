from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from phone_field import PhoneField
from django.contrib.auth.models import User


# Create your models here.

class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE,
                            verbose_name="فرزند")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(null=False, unique=True, verbose_name="اسلاگ")
    image = models.ImageField(upload_to='media/cat/', verbose_name='تصویر دسته', blank=True)
    fav = models.BooleanField(default=False, verbose_name='محبوب', blank=True)
    icon = models.CharField(max_length=20, blank=True, verbose_name='آیکون')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'slug': self.slug})

    def __str__(self):  # __str__ method elaborated later in
        full_path = [self.title]  # post.  use __unicode__ in place of
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class city(models.Model):
    title = models.CharField(max_length=100, verbose_name="اسم شهر")
    slug = models.SlugField(max_length=30, verbose_name='آدرس')
    image = models.ImageField(upload_to='media/city/', verbose_name='تصویر شهر', blank=True)
    fav = models.BooleanField(default=False, verbose_name='محبوب', blank=True)

    def get_absolute_url(self):
        return reverse('city-list')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'


class ImageGallery(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان")
    pic = models.ImageField(upload_to='upload/images', default='upload/images/no-img.jpg', verbose_name="تصویر")
    alt = models.CharField(max_length=200, null=True, blank=True, verbose_name="نام جایگزین")
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name="توضیحات")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'


class advertise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=100, verbose_name='عنوان آکهی')
    content = models.TextField(verbose_name="توضیحات")
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    city = models.ForeignKey(city, on_delete=models.CASCADE, verbose_name='شهر')
    price = models.DecimalField(max_digits=11, decimal_places=0, default=0, verbose_name="قیمت")
    category = models.ManyToManyField(Category, blank=True, verbose_name="دسته بندی")
    pic = models.ImageField(upload_to='upload/product/images', default='upload/images/no-img.jpg', verbose_name="تصویر")
    image_gallery = models.ManyToManyField(ImageGallery, blank=True, verbose_name="گالری تصاویر")
    phone = PhoneField(verbose_name="شماره تماس")
    email = models.EmailField(verbose_name='ایمیل')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='آدرس')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advertise-detail')

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = 'آگهی ها'
