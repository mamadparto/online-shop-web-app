from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status','active']


admin.site.register(Product, ProductAdmin)
