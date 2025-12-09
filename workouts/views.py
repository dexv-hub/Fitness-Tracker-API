from rest_framework import generics, permissions
from .serializers import WorkoutSerializer
from .models import Workouts
from stats.utils import filter_and_sort_queryset

class WorkoutsListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Workouts.objects.filter(user=self.request.user)
        sort_options = {
            "burned_calories_asc": "burned_calories",
            "burned_calories_desc": "-burned_calories",
            "duration_asc": "duration_minutes",
            "duration_desc": "-duration_minutes"
        }
        return filter_and_sort_queryset(
            queryset,
            self.request,
            date_field="date",
            sort_fields=sort_options
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workouts.objects.filter(user=self.request.user)
