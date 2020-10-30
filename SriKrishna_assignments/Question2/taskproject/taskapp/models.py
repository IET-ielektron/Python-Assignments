from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=100,null=True, blank=True,verbose_name='Employee Name')
    manager_id = models.ForeignKey("Employee",on_delete=models.CASCADE,
		verbose_name='Manager Id', null=True, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return str(self.emp_name)
