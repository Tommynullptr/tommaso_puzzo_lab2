from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from .models import CustomUser


class UserFormRegister(UserCreationForm, ModelForm):

    class Meta:

        model = CustomUser
        fields = '__all__'


class UserFormLogin(AuthenticationForm, forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)