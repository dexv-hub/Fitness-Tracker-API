from rest_framework import generics, permissions
from .serializers import BodySerializer
from .models import Body

class BodyListCreateView(generics.ListCreateAPIView):
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Body.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BodyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Body.objects.filter(user=self.request.user)