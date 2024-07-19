from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


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
        return reverse('product_detail', args=[self.id])


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
    active = models.BooleanField(default=True)



