from rest_framework import generics, permissions
from .models import Water
from .serializers import WaterSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    get=extend_schema(
        summary = "Retrieve user Water entries",
        description = "Returns all Water objects belonging to the authenticated user. ",
        responses = {200: WaterSerializer(many=True),
                    401: {"description": "Unauthorized — user must be authenticated"}},

    ),
    post=extend_schema(
        summary = "Create a new Water entry",
        description = "Creates a new Water record for the authenticated user.",
        request = WaterSerializer,
        responses = {201: WaterSerializer,
                    400: {"description": "Validation error"},
                    401: {"description": "Unauthorized — user must be authenticated"}},
    )
)

class WaterListCreateView(generics.ListCreateAPIView):
    serializer_class = WaterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Water.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve a Water entry",
        description = "Returns a single Water object owned by the authenticated user.",
        responses = {
            200: WaterSerializer,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Water entry not found"}}
    ),
    put = extend_schema(
        summary = "Update a Water entry",
        description = "Fully updates the Water object. All fields must be provided.",
        request = WaterSerializer,
        responses = {
            200: WaterSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Water entry not found"}}
    ),
    patch = extend_schema(
        summary = "Partially update a Water entry",
        description = "Partially updates the Water object. Only provided fields will be updated.",
        request = WaterSerializer,
        responses = {
            200: WaterSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Water entry not found"}}
    ),
    delete = extend_schema(
        summary = "Delete a Water entry",
        description = "Deletes the specified Water object owned by the authenticated user.",
        responses = {
            204: None,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Water entry not found"}}
    ),
)

class WaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WaterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Water.objects.filter(user=self.request.user)
