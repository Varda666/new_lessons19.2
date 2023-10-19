from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, UserUpdateView, generate_new_password, verificate_user

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('verification/', verificate_user, name='verification'),
    ]

