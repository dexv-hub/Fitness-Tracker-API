from rest_framework import serializers
from .models import Body

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ["id", "user", "weight", "date"]
        read_only_fields = ["id", "user"]