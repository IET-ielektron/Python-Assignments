from rest_framework import status, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

#view function (api_view type)
@api_view(['GET'])
def get_employee_list(request):
    try:
        emp_list = Employee.objects.all()
        # print(emp_list)
        try:
            serialized_data = EmployeeSerializer(emp_list, many=True)  # call serializer
        except:
            #raise
            msg = {'error': 'serializing data'}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        if not serialized_data:
            content = {'info': 'employee list not found'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    except:
        #raise
        content = {'error': 'internal server error occurred'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

