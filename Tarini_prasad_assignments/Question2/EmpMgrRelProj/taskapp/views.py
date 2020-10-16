from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .serializers import EmployeeSerializer

def home(request):
    return render(request,'taskapp/home.html')

# ------------- Retrive data from  EmployeeData table -----
def showemp(request):
    data = EmployeeData.objects.all()
    return render(request, 'taskapp/get_employee.html', {'data': data})


def postemp(request):
    if request.method == 'POST':
        fm = EmpForm(request.POST)
        if fm.is_valid():
            ename = fm.cleaned_data['ename']
            designation = fm.cleaned_data['designation']
            manager = fm.cleaned_data['manager']
            if not EmployeeData.objects.filter(designation='CEO').exists():
                obj = EmployeeData(ename=ename, designation=designation,manager=manager)
                obj.save()
            else:
                return HttpResponse("ceo already exist")
            return HttpResponseRedirect('/showemp')
    else:
        fm = EmpForm()
    return render(request, "taskapp/add_employee.html", {'form': fm})





@api_view(['GET'])
def empTypeApi(request):
    data = EmployeeData.objects.all()
    obj_lst = []
    for emp in data:
        obj = {"id": emp.id,'ename': emp.ename}
        if emp.manager:
            obj['manager'] = emp.manager.ename
        obj_lst.append(obj)
    return HttpResponse(json.dumps({"employeeList":obj_lst}),content_type="application/json")


