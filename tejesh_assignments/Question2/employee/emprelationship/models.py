from django.db import models

class Employee(models.Model):

    emp_id = models.IntegerField(primary_key=True, null=False)
    emp_name = models.CharField(max_length=150)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='employee')

    def __str__(self):
        return self.emp_name

