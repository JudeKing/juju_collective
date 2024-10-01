from django.shortcuts import render
from juju_warehouse.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    
    return render(request, 'pages/home.html', {'product': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'pages/shop.html',  {'products': products})