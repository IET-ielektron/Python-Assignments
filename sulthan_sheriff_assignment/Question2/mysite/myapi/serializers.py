from rest_framework import serializers

from .models import employee

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = ('employee_id', 'employee_name','manager_name')