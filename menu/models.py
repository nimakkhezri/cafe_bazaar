from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='توضیحات')
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True, verbose_name='آیکن')

    def __str__(self):
        return f'{self.name}: {self.description}'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='محصول')
    name = models.CharField(max_length=100, verbose_name='نام')
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return f'{self.category}: {self.name}'

class Type(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='types', verbose_name='محصول')
    name = models.CharField(max_length=20, verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')

    def __str__(self):
        return f'{self.product}: {self.name}'
