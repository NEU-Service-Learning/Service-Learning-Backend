from base.models import Record
from rest_framework import serializers
from base.record_category_serializer import RecordCategorySerializer


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'enrollment', 'project', 'date', 'start_time', 'total_hours', 'longitude', 'latitude',
                  'category', 'is_active', 'comments', 'extra_field')
