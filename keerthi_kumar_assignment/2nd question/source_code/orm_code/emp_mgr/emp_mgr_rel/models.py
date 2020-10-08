from django.db import models

#employee model recursive model
class Employee(models.Model):
    class Meta:
        verbose_name_plural = 'Employees'       #to display the table name

    emp_id = models.AutoField(primary_key=True)     #auto increment for primary key
    emp_name = models.CharField(max_length=100)
    manager_name = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)    #id is same as the emp_id as it has self

    def __str__(self):
        return self.emp_name  #display the emp_name


