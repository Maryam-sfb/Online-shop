from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.contrib import messages


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, 'You registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
