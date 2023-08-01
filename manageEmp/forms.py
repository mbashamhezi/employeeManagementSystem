from django import forms

class AssetAssignmentForm(forms.Form):
    employee_id = forms.IntegerField()
    asset_name = forms.CharField(max_length=100)
    asset_serial_number = forms.CharField(max_length=50)
    asset_model = forms.CharField(max_length=50)
