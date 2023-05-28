from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"), 

]
