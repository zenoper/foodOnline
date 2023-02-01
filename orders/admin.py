from django.contrib import admin
from .models import Payment, Order, OrderedFood

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'name', 'phone', 'email', 'order_to', 'total']

admin.site.register(Payment)
admin.site.register(OrderedFood)
admin.site.register(Order, OrderAdmin)
