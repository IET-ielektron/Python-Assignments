from django.contrib import admin

from taskapp.models import  Employee


class EmployeesAdmin(admin.ModelAdmin):
	list_display=[
				'id',
				'emp_name',
				'manager_id',
				]
	# readonly_fields = [
	# 			'emp_name',
	# 			'manager',
	# 		]

	# def has_delete_permission(self, request, obj=None):
	# 	return False
    #
	# def has_add_permission(self, request, obj=None):
	# 	return True
    #

admin.site.register(Employee, EmployeesAdmin)

