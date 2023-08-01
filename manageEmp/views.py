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
        return redirect('admin_dashboard')  # Replace 'employee_list' with the appropriate URL name for the employee list view
    return render(request, 'manageEmp/edit_employee.html', {'employee': employee})


def view_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'manageEmp/view_employee.html', {'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('admin_dashboard')  # Replace 'employee_list' with the appropriate URL name for the employee list view
    return render(request, 'manageEmp/delete_employee.html', {'employee': employee})


   
# def add_asset(request):
#     if request.method == 'POST':
#         employee_id = request.POST.get('employee_id')
#         assetName = request.POST.get('assetName')
#         sno = request.POST.get('sno')
#         model = request.POST.get('model')
        
#         asset = Asset(employee_id=employee_id, assetName=assetName, sno=sno, model=model )
#         asset.save()
#         return redirect('admin_dashboard')
#     return render(request, 'manageEmp/add_asset.html')

from django.shortcuts import render, redirect
from .models import Asset

def add_asset(request):
    if request.method == 'POST':
        id_number = request.POST['id']
        asset_name = request.POST['assetName']
        serial_number = request.POST['sno']
        model = request.POST['model']
        
        # Assuming you have a foreign key field named 'employee' in your Asset model
        # Retrieve the employee object based on the employee ID
        employee_id = 45  # Replace with the actual employee ID from your form or session
        employee = Employee.objects.get(id=employee_id)

        # Create a new Asset object and save it to the database
        asset = Asset(id_number=id_number, asset_name=asset_name, serial_number=serial_number, model=model, employee=employee)
        asset.save()

        return redirect('success')  # Redirect to a success page or any other desired URL
    
    return render(request, 'manageEmp/add_asset.html')  # Replace 'add_asset.html' with the path to your template











