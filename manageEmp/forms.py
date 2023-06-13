from django import forms
# from .models import Employee, Asset, Leave
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fname', 'role', 'email', 'password')

