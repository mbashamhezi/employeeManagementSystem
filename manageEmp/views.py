from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from .forms import EmployeeForm, AssetForm, LeaveForm
from .models import Employee, Asset 
 

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

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') # Redirects to the login page
    else:
        return redirect('signup')

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
     
# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, 'manageEmp/employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        role = request.POST.get('role')
        email = request.POST.get('email')
        pnumber = request.POST.get('pnumber')
        tpass = request.POST.get('tpass')
        employee = Employee(fname=fname, role=role, email=email, pnumber=pnumber, tpass=tpass)
        employee.save()
        return redirect('admin_dashboard')
    return render(request, 'manageEmp/add_employee.html')


   
def add_asset(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        assetName = request.POST.get('assetName')
        sno = request.POST.get('sno')
        model = request.POST.get('model')
        
        asset = Asset(id=id, assetName=assetName, sno=sno, model=model )
        asset.save()
        return redirect('admin_dashboard')
    return render(request, 'manageEmp/add_asset.html')






