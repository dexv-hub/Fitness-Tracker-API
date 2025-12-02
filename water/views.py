from rest_framework import generics, permissions
from .models import Water
from .serializers import WaterSerializer

class WaterListCreateView(generics.ListCreateAPIView):
    serializer_class = WaterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Water.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WaterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Water.objects.filter(user=self.request.user)
