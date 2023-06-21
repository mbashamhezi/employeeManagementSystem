from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column='employee_id')
    fname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pnumber = models.CharField(max_length=10, null=True)
    tpass = models.CharField(max_length=100)

class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


     


