from django.db import models
from datetime import datetime
# Create your models here.

class EmployeeAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()
    is_present = models.BooleanField(default=False)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (self.name)