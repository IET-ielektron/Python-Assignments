from .models import Employe
from django.core import serializers
from django.db import connection
from rest_framework import viewsets
from .serializers import JointableSerializer

# Create your views here.


class JointableViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset =  Employe.objects.raw('SELECT e.id ,e.name,e.managername  from employe e join employe e1 on e.managerid=e1.id;')
	serializer_class = JointableSerializer