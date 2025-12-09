from rest_framework import serializers
from .models import Water

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ["id", "user", "water_consumption", "date"]
        read_only_fields = ["id", "user"]
