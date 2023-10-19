from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import HiddenInput
from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'country', 'img')


        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            self.fields[1].widget = forms.HiddenInput()
