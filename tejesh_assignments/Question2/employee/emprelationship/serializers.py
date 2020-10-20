from rest_framework import serializers
from .models import Employee

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('emp_id', 'emp_name','manager')
        read_only_fields = ('manager',)
        depth = 1