from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Custom based api
from emp_mgr_rel.methods.list import get_emp_data

@api_view(['GET'])
def get(request):
    emp_list = get_emp_data()
    if emp_list:
        return Response(emp_list, status=status.HTTP_200_OK)
    else:
        content = {'empty'}
        return Response(content, status=status.HTTP_200_OK)