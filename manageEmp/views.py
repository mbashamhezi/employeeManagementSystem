from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Employee, Asset 
from django.shortcuts import render, get_object_or_404, redirect
 

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


def logout_view(request):
    logout(request)
    return redirect('home')


def admin_dashboard(request):
    if request.method == 'POST':
        return redirect('login')
    elif request.method == 'GET':
        employees = Employee.objects.all()
        assets = Asset.objects.all()
        context = { 
            'employees': employees,
            'assets': assets,
         }
        return render(request, 'manageEmp/admin_dashboard.html', context)


def add_employee(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        role = request.POST.get('role')
        email = request.POST.get('email')
        pnumber = request.POST.get('pnumber')
        tpass = request.POST.get('tpass')
        employee = Employee.objects.create(fname=fname, role=role, email=email, pnumber=pnumber, tpass=tpass)
        employee.save()
        return redirect('admin_dashboard')
    return render(request, 'manageEmp/add_employee.html')


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        # Update the employee's data based on the submitted form
        employee.fname = request.POST.get('fname')
        employee.role = request.POST.get('role')
        employee.email = request.POST.get('email')
        employee.pnumber = request.POST.get('pnumber')
        employee.save()
        return redirect('admin_dashboard') 
    return render(request, 'manageEmp/edit_employee.html', {'employee': employee})


def view_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'manageEmp/view_employee.html', {'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('admin_dashboard') 
    return render(request, 'manageEmp/delete_employee.html', {'employee': employee})


def add_asset(request):
    if request.method == 'POST':
        asset_name = request.POST['asset_name']
        serial_number = request.POST['serial_number']
        model = request.POST['model']
        asset = Asset(asset_name=asset_name, serial_number=serial_number, model=model)
        asset.save()
        return redirect('admin_dashboard')
    return render(request, 'manageEmp/add_asset.html')


def view_and_delete_asset(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    if request.method == 'POST' and 'delete' in request.POST:
        asset.delete()
        return redirect('admin_dashboard') 
    return render(request, 'manageEmp/view_and_delete_asset.html', {'asset': asset})












