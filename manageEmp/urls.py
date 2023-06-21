from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('logout', views.logout_view, name='logout'),
   path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"), 

   path('add_employee', views.add_employee, name='add_employee'),
   path('add_employee/<int:employee_id>/', views.add_employee, name='add_employee'),
   path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
   path('view_employee/<int:employee_id>/', views.view_employee, name='view_employee'),
   path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
   
   path('add_asset', views.add_asset, name='add_asset'),
]
