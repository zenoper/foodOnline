from django.contrib import admin
from .models import Payment, Order, OrderedFood

admin.site.register(Payment)
admin.site.register(OrderedFood)
admin.site.register(Order)
