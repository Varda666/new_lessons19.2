import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User
from users.services import _send_mail_email, _send_mail_password


class LoginView(BaseLoginView):
    #success_url = reverse_lazy('users:profile')
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        _send_mail_email(self.object.email)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    request.user.set_password(new_password)
    request.user.save()
    _send_mail_password(new_password, request.user.email)
    return redirect(reverse('users:login'))


def verificate_user(request):
    pk = request['pk']
    user = User.objects.get(pk=pk)
    user.is_verificated = True
    user.is_activated = True





