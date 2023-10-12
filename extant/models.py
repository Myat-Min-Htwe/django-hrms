from django.db import models
from datetime import datetime

# Create your models here.

class ExtantModel(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=100,default='...')
    phone_number = models.CharField(max_length=20,default=None)
    address = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return(self.name)