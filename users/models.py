from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=35, verbose_name='Номер телефона')
    country = models.CharField(max_length=35, verbose_name='Страна')
    img = models.ImageField(upload_to='media/', verbose_name='Аватар')
    email = models.EmailField(unique=True, verbose_name='email')
    is_verificated = models.BooleanField(default=False, verbose_name='Подтверждение почты')
    is_activated = models.BooleanField(default=False, verbose_name='Статус пользователя')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

