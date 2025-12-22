from rest_framework import generics, permissions
from .serializers import BodySerializer
from .models import Body
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve user Body entries",
        description = "Returns all Body objects belonging to the authenticated user.",
        responses = {200: BodySerializer(many=True),
                    401: {"description": "Unauthorized — user must be authenticated"}},

    ),
    post = extend_schema(
        summary = "Create a new Body entry",
        description = "Creates a new Body record for the authenticated user.",
        request = BodySerializer,
        responses = {201: BodySerializer,
                    400: {"description": "Validation error"},
                    401: {"description": "Unauthorized — user must be authenticated"}},
    ),
)

class BodyListCreateView(generics.ListCreateAPIView):
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Body.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve a Body entry",
        description = "Returns a single Body object owned by the authenticated user.",
        responses = {
            200: BodySerializer,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Body entry not found"}}
    ),
    put = extend_schema(
        summary = "Update a Body entry",
        description = "Fully updates the Body object. All fields must be provided.",
        request = BodySerializer,
        responses = {
            200: BodySerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Body entry not found"}}
    ),
    patch = extend_schema(
        summary = "Partially update a Body entry",
        description = "Partially updates the Body object. Only provided fields will be updated.",
        request = BodySerializer,
        responses = {
            200: BodySerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Body entry not found"}}
    ),
    delete = extend_schema(
        summary = "Delete a Body entry",
        description = "Deletes the specified Body object owned by the authenticated user.",
        responses = {
            204: None,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Body entry not found"}}
    ),
)

class BodyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BodySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Body.objects.filter(user=self.request.user)
