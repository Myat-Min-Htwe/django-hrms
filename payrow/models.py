from django.db import models

# Create your models here.


class Payrow(models.Model):
    name = models.CharField(max_length=30)
    pay_date = models.DateField()
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    paystub = models.ImageField(default=None, blank=True)

    def __str__(self):
        return self.name
