from django.db import models
from django.urls import reverse


status = (
    ('available', 'available'),
    ('unavailable', 'unavailable'),
    ('coming_soon', 'comming soon')
)
class Product(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=12 , choices=status)


    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
