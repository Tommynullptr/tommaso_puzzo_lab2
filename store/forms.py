from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


#class UserFormRegister(forms.ModelForm):

    #password = forms.CharField(widget=forms.PasswordInput)

    #class Meta:

   #     model = User
  #      fields = ['username', 'firstname', 'lastname', 'password', 'address', 'city', 'state']


class UserFormLogin(AuthenticationForm, forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)