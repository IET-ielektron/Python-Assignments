#convert the data to json before transfering it to api
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField()  # get ForeignKey value instead id (manager name instead of manager id) in result
    emp_id = serializers.CharField(source='id') # alias id by emp_id
    class Meta:
        model=Employee # name of the model
        fields = ['emp_id','emp_name','manager'] # column names to be fetched
        #depth = 1
