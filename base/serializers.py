from django.contrib.auth.models import User
from rest_framework import serializers

"""
    THESE ARE JUST EXAMPLES, PLEASE REPLACE
"""
class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    instructors = serializers.PrimaryKeyRelatedField(many=True, queryset=Instructor.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'courses', 'instructors')

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created = serializers.ReadOnlyField()
    instructors = serializers.PrimaryKeyRelatedField(many=True, queryset=Instructor.objects.all())

    class Meta:
        model = Course
        fields = ('id', 'created', 'owner', 'instructors')

class InstructorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    instructor = serializers.ReadOnlyField(source='instructor.id')
    created = serializers.ReadOnlyField()
    is_positive = serializers.BooleanField()

    class Meta:
        model = Instructor
        fields = ('id', 'created', 'owner', 'instructor', 'is_positive')
