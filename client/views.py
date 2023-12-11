from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = UserRegisterForm
    template_name = 'client/create_user.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user.save()
        login(self.request, user)
        return redirect('home')
    

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'client/auth_user.html'

    def get_success_url(self):
        return '/'


def logout_user(request):
    logout(request)
    return redirect('auth_user')