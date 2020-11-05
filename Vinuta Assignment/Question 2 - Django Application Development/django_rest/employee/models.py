from django.db import models

# Create your models here.

''' create table and self join employee-manager and get manager name'''
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    manager = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING) # ForeignKey

    def __str__(self):
        return self.emp_name
