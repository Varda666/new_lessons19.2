import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User


class LoginView(BaseLoginView):
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
        send_mail(
            subject='Поздравление',
            message=f'Подтвердите вашу почту и перейдите по ссылке http://127.0.0.1:8000/users/verification/{self.object.id}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9) for _ in range(6))])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль{new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:profile'))


def verificate_user(request):
    pk = request['pk']
    user = User.objects.get(pk=pk)
    user.is_verificated = True
    user.is_activated = True





