from rest_framework import serializers
from .models import Workouts

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workouts
        fields = ["id", "user", 'workout_type', "duration_minutes", "burned_calories", "date"]
        read_only_fields = ["id", "user"]