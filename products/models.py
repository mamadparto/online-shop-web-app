from django.db import models



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


    datetime_created = models.DateTimeField(auto_created=True)
    datetime_modified = models.DateTimeField(auto_created=True)