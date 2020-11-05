from employee.models import Employee
from employee.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

# get request
@api_view(['GET'])
def employee_details(request):
    try:
        emp = Employee.objects.exclude(manager_id__isnull=True) # get all data from the table whose manager_is is not null
        serializers = EmployeeSerializer(emp, many=True) # send the queryset to serializer to convert to json object
        return Response(serializers.data)
    except Exception as e:
        return Response(str(e))
