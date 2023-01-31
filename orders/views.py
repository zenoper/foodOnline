from django.shortcuts import render, redirect
from marketplace.models import Cart
from .forms import OrderForm
from .models import Order
from marketplace.context_processors import get_cart_amount
from .utils import generate_order_number
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

# Create your views here.

@login_required(login_url='login')
def place_order(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('marketplace')
    
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
            order.save()
            order.order_number = generate_order_number(order.id)
            order.save()
            context = {
                'order': order,
                'cart_items': cart_items,
            }
            return render(request, 'orders/place_order.html', context)
        else:
            print(form.errors)
    return render(request, 'orders/place_order.html')

def order_complete(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('created_at')

    cart_items.delete()
    return render(request, 'orders/order_complete.html')