from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"), 
   path('add_employee', views.add_employee, name='add_employee'),
   # path('employees', views.employee_list, name='employees'),
   path('add_asset', views.add_asset, name='add_asset'),
   # path('assets', views.asset_list, name='assets'),
]
