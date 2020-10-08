from django.urls import path
from . import views

urlpatterns = [
    #get the employee lists
    path('employee/list', views.get_employee_list, name='employee_list')
    ]