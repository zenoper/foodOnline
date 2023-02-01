from django.shortcuts import render, redirect
from marketplace.models import Cart
from .forms import OrderForm
from .models import Order
from marketplace.context_processors import get_cart_amount
from .utils import generate_order_number
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from menu.models import FoodItem
import json

# Create your views here.

@login_required(login_url='login')
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('marketplace')
    
    vendor_ids = []

    for i in cart_items:
        if i.fooditem.vendor.id not in vendor_ids:
            vendor_ids.append(i.fooditem.vendor.id)

    subtotal = 0
    k = {}
    total_data = {}
    for i in cart_items:
        fooditem = FoodItem.objects.get(pk=i.fooditem.id, vendor_id__in=vendor_ids)
        v_id = fooditem.vendor.id
        if v_id in k:    
            subtotal = k[v_id]
            subtotal += (fooditem.price * i.quantity)
            k[v_id] = subtotal
        else:
            subtotal = (fooditem.price * i.quantity)
            k[v_id] = subtotal
    
        total_data.update({fooditem.vendor.id: str(subtotal)})

    
    grand_total = get_cart_amount(request)['grand_total']
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order()
            order.first_name = form.cleaned_data['first_name']
            order.last_name = form.cleaned_data['last_name']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.address = form.cleaned_data['address']
            order.country = form.cleaned_data['country']
            order.state = form.cleaned_data['state']
            order.city = form.cleaned_data['city']
            order.pin_code = form.cleaned_data['pin_code']
            order.user = request.user
            order.total = grand_total
            order.total_data = json.dumps(total_data)
            order.save()
            order.order_number = generate_order_number(order.id)
            order.vendors.add(*vendor_ids)
            order.save()
            context = {
                'order': order,
                'cart_items': cart_items,
                'total_data': total_data,
            }
            return render(request, 'orders/place_order.html', context)
        else:
            print(form.errors)
    return render(request, 'orders/place_order.html')

def order_complete(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')

    cart_items.delete()
    return render(request, 'orders/order_complete.html')