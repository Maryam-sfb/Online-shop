from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.cart_session import Cart
from .models import Order, OrderItem, Coupon
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages


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
    form = CouponForm()
    return render(request, 'orders/order.html', {'order': order, 'form': form})


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)  # lte = lower than or equal to
        except Coupon.DoesNotExist:
            messages.error(request, 'This coupon does not exist!', 'danger')
            return redirect('orders:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
        return redirect('orders:detail', order_id)


















