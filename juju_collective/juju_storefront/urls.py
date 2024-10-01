from . import views
from django.urls import path
from django.contrib import admin

app_name = 'storefront'
urlpatterns = [
    path('', views.home, name="home"),
    path('shop', views.shop, name="shop"),
]