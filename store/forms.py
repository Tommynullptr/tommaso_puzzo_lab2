from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class UserFormRegister(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = CustomUser
        fields = ['username', 'firstname', 'lastname', 'password', 'address', 'city', 'state']


class UserFormLogin(AuthenticationForm, forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)