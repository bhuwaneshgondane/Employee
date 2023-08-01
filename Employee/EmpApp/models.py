from django.db import models

# Create your models here.
class EmployeeM(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=6)
    emp_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()