from rest_framework import generics, permissions
from .serializers import WorkoutSerializer
from .models import Workouts
from stats.utils import filter_and_sort_queryset
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get = extend_schema(
        summary = 'Retrieve user Workouts entries',
        description = "Returns all Workouts objects belonging to the authenticated user."
                      "Supports sorting via query parameters such as "
                      "`burned_calories_asc`, `burned_calories_desc`, "
                      "`duration_asc`, `duration_desc`.",
        responses = {200: WorkoutSerializer(many=True),
                    401: {"description": "Unauthorized — user must be authenticated"}},
    ),
    post = extend_schema(
        summary = "Create a new Workouts entry",
        description = "Creates a new Workouts record for the authenticated user.",
        request = WorkoutSerializer,
        responses = {201: WorkoutSerializer,
                    400: {"description": "Validation error"},
                    401: {"description": "Unauthorized — user must be authenticated"}},
    )
)

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

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve a Workouts entry",
        description = "Returns a single Workouts object owned by the authenticated user.",
        responses = {
            200: WorkoutSerializer,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Workouts entry not found"}}
    ),
    put = extend_schema(
        summary ="Fully update a Workouts entry",
        description = "Fully updates the Workouts object. All fields must be provided.",
        request = WorkoutSerializer,
        responses = {
            200: WorkoutSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Workouts entry not found"}}
    ),
    patch = extend_schema(
        summary = "Partially update a Workouts entry",
        description = "Partially updates the Workouts object. Only provided fields will be updated.",
        request = WorkoutSerializer,
        responses = {
            200: WorkoutSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Workouts entry not found"}}
    ),
    delete = extend_schema(
        summary = "Delete a Workouts entry",
        description = "Deletes the specified Workouts object owned by the authenticated user.",
        responses = {
            204: None,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Workouts entry not found"}}
    ),
)

class WorkoutsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workouts.objects.filter(user=self.request.user)
