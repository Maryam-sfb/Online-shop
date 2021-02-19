from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.home, name='category_filter'),
    path('<slug:myslug>/', views.ProductDetail.as_view(), name='product_detail'),
]
