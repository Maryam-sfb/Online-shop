from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_filter', args=[self.slug,])


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته بندی')
    name = models.CharField(max_length=200, verbose_name='نام')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='عکس')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    available = models.BooleanField(default=True,verbose_name='در دسترس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])