
from . import views
from django.urls import path

app_name = 'client'

urlpatterns = [
    path('', views.login_user, name="login_user"),
    path('authenticate_user', views.authenticate_user,
        name="authenticate_user"),
    path('/register', views.register, name="register"),
    path('/dashboard', views.dashboard, name="dashboard"),
    path('/add_product', views.add_product, name="add_product"),
    path('logout/', views.logout_user, name='logout_user'),
]
