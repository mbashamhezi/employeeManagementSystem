from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .models import Employee, Asset, Leave
# from django.db import models

def home(request):
    return render(request, "manageEmp/signup.html")

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        position = request.POST['position']
        company = request.POST['company']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        pass1 = request.POST['password']

        myuser = User.objects.create_user(username=fname, email=email, password=pass1)
        myuser.full_name = fname
        myuser.position = position
        myuser.company = company
        myuser.phone_number = pnumber

        myuser.save()
        messages.success(request, "Your account is created successfully.")

        return redirect('signin')
    return render(request, "manageEmp/signup.html")

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['password']
        user = authenticate(request, username=email, password=pass1)
        if user is not None:
            login(request, user)
        return redirect('admin_dashboard')  # Redirect to home page after successful login
    else:
        messages.error(request, 'Invalid credentials')
    return render(request, "manageEmp/signin.html")

def admin_dashboard(request):
    return render(request, "manageEmp/admin_dashboard.html")

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') # Redirects to the login page
    else:
        return redirect('signup')

# def user_dasboard(request):
#     if request.method == 'POST':
#         if 'add_employee' in request.POST:
#             # Handle adding an employee
#             fname = request.POST.get('fname')
#             role = request.POST.get('role')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
            
#             # Create a new employee object
#             employee = Employee.objects.create(fname=fname, role=role, email=email, password=password)
#             employee.save()
            
#         elif 'add_asset' in request.POST:
#             # Handle adding an asset
#             asset = request.POST.get('asset')
            
#             # Create a new asset object
#             asset = Asset.objects.create(asset_name=asset)
#             asset.save()
            
#         elif 'add_leave' in request.POST:
#             # Handle adding leave
#             days = request.POST.get('days')
            
#             # Create a new leave object
#             leave = Leave.objects.create(days=days)
#             leave.save()

#     return render(request, 'myapp/home.html')
