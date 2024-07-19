from django.contrib import admin

from .models import Product, ProductComment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status','active']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'stars', 'active']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment, )
