from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .forms import EmployeeForm, AssetForm, LeaveForm
# from .models import Employee, Asset, Leave
from django.db import models
from .models import Employee
from .forms import EmployeeForm

def home(request):
    return render(request, "manageEmp/signup.html")

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        username = request.POST['username']
        position = request.POST['position']
        company = request.POST['company']
        email = request.POST['email']
        pnumber = request.POST['pnumber']
        pass1 = request.POST['password']

        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.full_name = fname
        myuser.username = username
        myuser.position = position
        myuser.company = company
        myuser.phone_number = pnumber

        myuser.save()
        messages.success(request, "Your account is created successfully.")

        return redirect('signin')
    return render(request, "manageEmp/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            request.session['error_message'] = 'Invalid username or password.'
            return redirect('signin') 
    
    # Get the error message from the session
    error_message = request.session.pop('error_message', None)
    
    return render(request, 'manageEmp/signin.html', {'error_message': error_message})

# def signin(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         pass1 = request.POST['password']
#         user = authenticate(request, username=email, password=pass1)
#         if user is not None:
#             login(request, User)
#         return redirect('admin_dashboard')  # Redirect to home page after successful login
#     else:
#         messages.error(request, 'Invalid credentials')
#     return render(request, "manageEmp/signin.html")

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') # Redirects to the login page
    else:
        return redirect('signup')

def admin_dashboard(request):
    if request.method == 'POST':
        # Handle adding an employee
        fname = request.POST.get('fname')
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
            
            # Create a new employee object
        employee = Employee(fname=fname, role=role, email=email, password=password)
        employee.save()
        return redirect('login')
    return render(request, 'manageEmp/admin_dashboard.html')


    # main content
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'home' with the URL you want to redirect to after saving the data
    else:
        form = EmployeeForm()
    return render(request, 'manageEmp/add_employee.html', {'form': form})

# def add_asset_view(request):
#     if request.method == 'POST':
#         form = AssetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Replace 'home' with the URL you want to redirect to after saving the data
#     else:
#         form = AssetForm()
#     return render(request, 'add_asset.html', {'form': form})

# def add_leave_view(request):
#     if request.method == 'POST':
#         form = LeaveForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Replace 'home' with the URL you want to redirect to after saving the data
#     else:
#         form = LeaveForm()
#     return render(request, 'add_leave.html', {'form': form})



