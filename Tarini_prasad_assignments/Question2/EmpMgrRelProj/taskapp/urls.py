from django.urls import path
from taskapp import views
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('addemp/', views.postemp, name='addemp'),
    path('showemp/', views.showemp, name='showemp'),
    path('api/', views.empTypeApi, name='custom'),
]
