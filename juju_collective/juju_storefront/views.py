from django.shortcuts import render
from juju_warehouse.models import Product

# Create your views here.
def home(request):
    """Render the home page displaying all products.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Rendered home page with products.
        :rtype: HttpResponse
    """
    products = Product.objects.all()
    
    return render(request, 'pages/home.html', {'product': products})

def shop(request):
    """Render the shop page displaying all products.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Rendered shop page with products.
        :rtype: HttpResponse
    """
    products = Product.objects.all()
    return render(request, 'pages/shop.html',  {'products': products})