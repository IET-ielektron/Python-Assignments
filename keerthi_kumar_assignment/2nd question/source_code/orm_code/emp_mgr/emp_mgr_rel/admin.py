from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'manager_name') #display the columns in db for table

admin.site.register(Employee, EmployeeAdmin) #register model to show up in admin panel
