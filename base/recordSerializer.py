from django.contrib.auth.models import Record
from django.contrib.auth.models import User
from rest_framework import serializers
from base.enrollmentSerializer import EnrollmentSerializer
from base.projectSerializer import ProjectSerializer
from base.recordCategorySerializer import RecordCategorySerializer

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'enrollment', 'project', 'date', 'start_time', 'total_hours', 'longitude', 'latitude',
                  'category', 'is_active', 'comments', 'extra_field')

