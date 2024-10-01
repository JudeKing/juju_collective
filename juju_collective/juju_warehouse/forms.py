from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Enter your name',
            'password1': 'Create a password',
            'password2': 'Confirm password'
        }

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = [
                'product_name', 
                'product_description', 
                'product_price',
                'product_image'
            ]


   