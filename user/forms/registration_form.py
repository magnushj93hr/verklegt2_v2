from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "password", "email")
