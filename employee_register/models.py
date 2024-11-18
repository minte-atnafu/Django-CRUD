from django.db import models

# Create your models here.

class Postion(models.Model):
    title = models.CharField(max_length=50)


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=15)
    postion = models.ForeignKey(Postion, on_delete=models.CASCADE)