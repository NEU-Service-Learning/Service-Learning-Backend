from base.models import College
from rest_framework import serializers

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name',)
