from rest_framework import serializers
#
from .models import Employee

#serializer class
class EmployeeSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(read_only=True, source='manager_name.emp_name') #relates the foreign key to the primary key and extraxt the manager name
    class Meta:
        model = Employee  #model name
        fields = ('emp_id', 'emp_name', 'manager')  #fields to be serilized for view
