from django.urls import reverse
from django.contrib import messages
from .forms import ProductUploadForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
def login_user(request):
    """Render the login page or redirect authenticated users to the 
       dashboard.
       
        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Redirects to the dashboard or renders the login page.
        :rtype: HttpResponse
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(
            reverse('client:dashboard')
        )
    else:
        return render(request, 'authentication/login.html')
    
def register(request):
    """Handle user registration.

        If successful, redirect to the login page with a success 
        message. If the method is GET, render the registration form.
    
        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Redirects to the login page or renders the registration
                 page.
        :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created!')
            return HttpResponseRedirect(
                reverse('client:login_user')
                )
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'authentication/register.html', context)

def logout_user(request):
    """Log out the user and redirect to the previous page or home.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Redirects to the previous page or home.
        :rtype: HttpResponse
    """

    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def authenticate_user(request):
    """Authenticate a user and log them in.

        :param request: The Http request object.
        :type request: HttpRequest
        :return: Redirects to the dashboard or the login page with an
                 error.
        :rtype: HttpResponse
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        messages.error(request,
'''The username or password provided was incorrect!
Please try again!
'''
                       )
        return HttpResponseRedirect(
            reverse('client:login_user')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('client:dashboard')
        )

def dashboard(request):
    """Render the user dashboard.

        If the user is authenticated, render the dashboard with a 
        product upload form. If not, redirect to the login page with an
        error message.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Rendered dashboard or login page with error message.
        :rtype: HttpResponse
    """

    if request.user.is_authenticated:
        form = ProductUploadForm()
        return render(request, 'pages/dashboard.html', {'form': form})   
    else:
        error_message = "You need to sign in first!"
        return render(
            request, 'authentication/login.html', {'error_message': error_message}
            )

def add_product(request):
    """Add a new product to the inventory.
    
        Attempt to save the product data from the provided form. If 
        successful, redirect to the dashboard.

        :param request: The HTTP request object.
        :type request: HttpRequest
        :return: Redirects to the dashboard after adding the product.
        :rtype: HttpResponse
    """
    if request.method == 'POST':
        # Allow files to be uploaded as well.
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save form to the database.
            form.save()
            messages.success(request, f'Product added!')
    else:
        form = ProductUploadForm()
    
    return HttpResponseRedirect(
            reverse('client:dashboard')
        )

        