from rest_framework import serializers
from .models import Sleep

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ['id', 'user', 'start_time', 'end_time', 'duration_hours']
        read_only_fields = ['id', 'user', 'duration_hours']