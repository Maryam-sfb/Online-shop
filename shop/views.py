from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Category
from cart.forms import CartAddForm

#class Home(TemplateView):
#    template_name = 'shop/home.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['products'] = Product.objects.filter(available=True)
#        context['categories'] = Category.objects.all()
#        return context


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})













