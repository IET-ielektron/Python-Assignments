from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(EmployeeData)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('ename','designation','manager')

admin.site.register(Designation)