from .serializers import NutritionSerializer
from rest_framework import generics, permissions
from .models import Nutrition
from stats.utils import filter_and_sort_queryset

class NutritionListCreateView(generics.ListCreateAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Nutrition.objects.filter(user=self.request.user)
        sort_options = {
            "calories_asc": "calories",
            "calories_desc": "-calories",
            "protein_asc": "protein",
            "protein_desc": "-protein"
        }
        return filter_and_sort_queryset(queryset, self.request, date_field="date", sort_fields=sort_options)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NutritionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)