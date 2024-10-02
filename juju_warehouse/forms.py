from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """Registers a user with username, password and confirm password.

        :class: 'UserCreationForm' is used to validate the form inputs.

        :param UserCreationForm: A form for user creation.

        :returns: A user in the database.
        :rtype: User
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Enter your name',
            'password1': 'Create a password',
            'password2': 'Confirm password'
        }

class ProductUploadForm(forms.ModelForm):
    """Uploads a product with name, description, price and image of the
       product.


        :class: 'forms.ModelForm' is used to validate the form inputs.

        :param product_name: The name of the product.
        :type product_name: str
        :param product_description: A description of the product.
        :type product_name: str
        :param product_price: The price of the product.
        :type product_price: int
        :param product_image: The image of the product 
        :type product_price: ImageField

        :returns: A new product in the database.
        :rtype: Product

    """
    class Meta:
        model = Product 
        fields = [
                'product_name', 
                'product_description', 
                'product_price',
                'product_image'
            ]


   