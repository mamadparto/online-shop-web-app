from typing import Any, MutableMapping
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


status = (
    ('available', 'available'),
    ('unavailable', 'unavailable'),
    ('coming_soon', 'comming soon')
)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Product(models.Model):
    title = models.CharField(max_length=150)
    discription = RichTextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    discount_percent = IntegerRangeField(default=0,min_value=1, max_value=30 ,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=12 , choices=status)
    cover = models.ImageField(verbose_name='product image', upload_to='product/product_cover/', blank=True)



    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentsManagetr(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManagetr, self).get_queryset().filter(active = True)


class ProductComment(models.Model):

    Product_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect')
    ]
    product = models. ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name= 'comments', )
    body = models.TextField()
    stars = models.CharField(max_length=10, choices=Product_STARS)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    objects = models.Manager()
    active_comments_managet = ActiveCommentsManagetr()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])





