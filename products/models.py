from django.db import models
from catalog.models import *

class Product(models.Model):
    name = models.CharField(max_length=50, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discriptions = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    subcategory = models.ForeignKey(Subcategory, models.SET_NULL, blank=True, null=True, default='subcategory')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to = 'products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % (self.product.name)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
