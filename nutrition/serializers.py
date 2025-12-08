from rest_framework import serializers
from .models import Nutrition

class NutritionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrition
        fields = ['id', 'user', 'calories', 'carbohydrates', 'protein', 'fats', "date"]
        read_only_fields = ['id', 'user', "date"]