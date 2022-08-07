from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm as ucf
from django.contrib.auth.models import User
from django import forms

class orderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'
        

class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(ucf):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
