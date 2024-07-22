from django.contrib import admin

from .models import Product, ProductComment


class ProductCommentsInline(admin.TabularInline):
    model = ProductComment
    fields = ['author', 'body', 'stars', 'active']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status','active']

    inlines = [
        ProductCommentsInline,
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'stars', 'active']



admin.site.register(Product, ProductAdmin)
admin.site.register(ProductComment, CommentAdmin)
