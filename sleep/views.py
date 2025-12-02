from rest_framework import generics, permissions
from .models import Sleep
from .serializers import SleepSerializers

class SleepListCreateView(generics.ListCreateAPIView):
    serializer_class = SleepSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sleep.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SleepDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SleepSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sleep.objects.filter(user=self.request.user)

