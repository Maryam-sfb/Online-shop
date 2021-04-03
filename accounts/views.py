from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, reverse
from .forms import UserRegistrationForm, ProfileForm
from .models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        messages.success(self.request, f'Welcome {user.full_name}!', 'success')
        if user.is_admin:
            return reverse_lazy('shop:home')
        else:
            return reverse_lazy('accounts:profile')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password'], cd['address'], cd['phone_number'])
            user.save()
            messages.success(request, 'You registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'accounts/profile.html'

    def get_object(self):  # to only show the profile of logged in user
        return User.objects.get(pk=self.request.user.pk)

    def get_success_url(self):
        messages.success(self.request, 'your account got updated successfully.', 'success')
        return reverse('shop:home')

    def get_form_kwargs(self):  # to send request.user to ProfileForm through kwargs
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs











