from base.models import Enrollment
from rest_framework import serializers

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id', 'user', 'course', 'semester', 'is_active', 'crn', 'meeting_days', 'meeting_start_time', 'meeting_end_time', 'required_hours')

class SectionSerializer(serializers.ModelSerializer):
    professor = serializers.SerializerMethodField('get_full_name')
    class Meta:
        model = Enrollment
        fields = ('professor', 'meeting_days', 'meeting_start_time', 'meeting_end_time', 'crn', 'required_hours')
    def get_full_name(self, obj):
        return obj.user.get_full_name()
