from django.shortcuts import render

from django.http import HttpResponse


from rest_framework import viewsets
from django.db.models import Q
from .serializers import employeeSerializer
from .models import employee


class ManagerViewSet(viewsets.ModelViewSet):

    queryset = employee.objects.filter(Q(manager_name='D')|Q(manager_name='B')|Q(manager_name='None(CEO)')).order_by('employee_name')
    print(queryset)
    serializer_class = employeeSerializer




# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def empl(request):
#     return HttpResponse("Hello, world")