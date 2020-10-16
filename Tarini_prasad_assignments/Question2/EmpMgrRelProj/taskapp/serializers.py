from rest_framework import serializers

from .models import *

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeData
        fields = '__all__'