from django.shortcuts import render

from .models import Employee
from rest_framework.views import APIView
from . serializers import employeesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
    
@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Employee.objects.all()
        serializer = employeesSerializer(snippets, many=True)
        return Response(serializer.data)