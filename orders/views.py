from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart_session import Cart
from .models import Order, OrderItem


@login_required(login_url='accounts:login')
def create_order(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        # cart.clear()
        return redirect('orders:detail', order.id)


@login_required(login_url='accounts:login')
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {'order': order})
