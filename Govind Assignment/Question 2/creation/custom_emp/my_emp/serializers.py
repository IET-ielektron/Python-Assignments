from rest_framework import serializers
from .models import Employe


class JointableSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employe
		fields = ['id','name','managername']
