from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pnumber = models.CharField(max_length=10, null=True)
    tpass = models.CharField(max_length=100)

class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    assetName = models.CharField(max_length=100)
    sno = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
     


