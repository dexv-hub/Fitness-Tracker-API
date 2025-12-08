from .serializers import NutritionSerializer
from rest_framework import generics, permissions
from .models import Nutrition

class NutritionListCreateView(generics.ListCreateAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NutritionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)