from django.db import models
from django.conf import settings
from shop.models import Product


class Order(models.Model):
    TYPE = (
        ('online', 'Online'),
        ('onsite', 'On Site')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    pay_type = models.CharField(max_length=100, choices=TYPE, default='online')

    def __str__(self):
        return f'{self.user} ordered {self.id}'

    def get_total_price(self):
        s = 0
        for item in self.items.all():
            s += item.get_cost()
        return s


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



