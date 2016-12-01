from django.contrib.auth.models import User
from base.models import *
from rest_framework import serializers

"""
    THESE ARE JUST EXAMPLES, PLEASE REPLACE
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'enrollment_set')
