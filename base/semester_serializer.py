from base.models import Semester
from django.contrib.auth.models import User
from rest_framework import serializers

class SemesterSerializer(serializers.ModelSerializer):
	
    class Meta:
	    model = Semester
	    fields = ('id', 'name', 'start_date', 'end_date', 'is_active')

