from base.models import Enrollment
from rest_framework import serializers

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('user', 'course', 'semester', 'is_active', 'crn')
