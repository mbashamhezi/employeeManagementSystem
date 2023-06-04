from django import forms
# from .models import Employee, Asset, Leave
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'role', 'email', 'password']

# class AssetForm(forms.ModelForm):
#     class Meta:
#         model = Asset
#         fields = ['asset']

# class LeaveForm(forms.ModelForm):
#     class Meta:
#         model = Leave
#         fields = ['days']
