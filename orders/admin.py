from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',  'first_name','last_name','is_paid', 'datetime_created']

    inlines = [
        OrderItemInline,
    ]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
