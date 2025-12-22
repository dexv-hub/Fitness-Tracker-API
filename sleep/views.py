from rest_framework import generics, permissions
from .models import Sleep
from .serializers import SleepSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary = "Retrieve user Sleep entries",
        description =
        "Returns all Sleep objects belonging to the authenticated user. ",
        responses = {200: SleepSerializer(many=True),
                    401: {"description": "Unauthorized — user must be authenticated"}},

    ),
    post=extend_schema(
        summary = "Create a new Sleep entry",
        description = "Creates a new Sleep record for the authenticated user.",
        request = SleepSerializer,
        responses = {201: SleepSerializer,
                    400: {"description": "Validation error"},
                    401: {"description": "Unauthorized — user must be authenticated"}},
    )
)


class SleepListCreateView(generics.ListCreateAPIView):
    serializer_class = SleepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sleep.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve a Sleep entry",
        description = "Returns a single Sleep object owned by the authenticated user.",
        responses = {
            200: SleepSerializer,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Sleep entry not found"}}
    ),
    put = extend_schema(
        summary = "Update a Sleep entry",
        description = "Fully updates the Sleep object. All fields must be provided.",
        request = SleepSerializer,
        responses = {
            200: SleepSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Sleep entry not found"}}
    ),
    patch = extend_schema(
        summary = "Partially update a Sleep entry",
        description = "Partially updates the Sleep object. Only provided fields will be updated.",
        request = SleepSerializer,
        responses = {
            200: SleepSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Sleep entry not found"}}
    ),
    delete = extend_schema(
        summary = "Delete a Sleep entry",
        description = "Deletes the specified Sleep object owned by the authenticated user.",
        responses = {
            204: None,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Sleep entry not found"}}
    ),
)

class SleepDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SleepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Sleep.objects.filter(user=self.request.user)

