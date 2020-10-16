from django.db import models

# Create your models here.
class Designation(models.Model):
    dept                    = models.CharField(max_length=100)

    def __str__(self):
        return self.dept

class EmployeeData(models.Model):
    ename                    =  models.CharField(max_length=100)
    designation              =  models.CharField(max_length=100)
    manager                  =  models.ForeignKey('self', null=True,blank=True, related_name='employee',on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

