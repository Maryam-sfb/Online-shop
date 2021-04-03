from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:home'), name='logout'),
    path('register/', views.user_register, name='register'),
]