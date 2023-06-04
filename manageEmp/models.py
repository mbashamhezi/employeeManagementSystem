from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# class Asset(models.Model):
#     asset = models.CharField(max_length=100)

# class Leave(models.Model):
#     days = models.CharField(max_length=100)
