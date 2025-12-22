from .serializers import NutritionSerializer
from rest_framework import generics, permissions
from .models import Nutrition
from stats.utils import filter_and_sort_queryset
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary = "Retrieve user Nutrition entries",
        description =
        "Returns all Nutrition objects belonging to the authenticated user. "
        "Supports optional sorting by calories, protein, fats, and carbohydrates, "
        "and filtering by date.",
        responses = {200: NutritionSerializer(many=True),
                    401: {"description": "Unauthorized — user must be authenticated"}},

    ),
    post=extend_schema(
        summary = "Create a new Nutrition entry",
        description = "Creates a new Nutrition record for the authenticated user.",
        request = NutritionSerializer,
        responses = {201: NutritionSerializer,
                    400: {"description": "Validation error"},
                    401: {"description": "Unauthorized — user must be authenticated"}},
    )
)

class NutritionListCreateView(generics.ListCreateAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Nutrition.objects.filter(user=self.request.user)
        sort_options = {
            "calories_asc": "calories",
            "calories_desc": "-calories",
            "protein_asc": "protein",
            "protein_desc": "-protein",
            "fats_asc": "fats",
            "fats_desc": "-fats",
            "carbohydrates_asc": "carbohydrates",
            "carbohydrates_desc": "-carbohydrates"


        }
        return filter_and_sort_queryset(queryset, self.request, date_field="date", sort_fields=sort_options)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    get = extend_schema(
        summary = "Retrieve a Nutrition entry",
        description = "Returns a single Nutrition object owned by the authenticated user.",
        responses = {
            200: NutritionSerializer,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Nutrition entry not found"}}
    ),
    put = extend_schema(
        summary = "Update a Nutrition entry",
        description = "Fully updates the Nutrition object. All fields must be provided.",
        request = NutritionSerializer,
        responses = {
            200: NutritionSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Nutrition entry not found"}}
    ),
    patch = extend_schema(
        summary = "Partially update a Nutrition entry",
        description = "Partially updates the Nutrition object. Only provided fields will be updated.",
        request = NutritionSerializer,
        responses = {
            200: NutritionSerializer,
            400: {"description": "Validation error"},
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Nutrition entry not found"}}
    ),
    delete = extend_schema(
        summary = "Delete a Nutrition entry",
        description = "Deletes the specified Nutrition object owned by the authenticated user.",
        responses = {
            204: None,
            401: {"description": "Unauthorized — user must be authenticated"},
            404: {"description": "Nutrition entry not found"}}
    ),
)

class NutritionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NutritionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Nutrition.objects.filter(user=self.request.user)