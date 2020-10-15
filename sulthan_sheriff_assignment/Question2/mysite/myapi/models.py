from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User


# Create your models here.
class employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=60)
    manager_name = models.CharField(max_length=60)


    # def __str__(self):
    #     return self.name


