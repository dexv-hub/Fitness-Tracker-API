from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from datetime import date
from nutrition.models import Nutrition
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(
        summary="Retrieve daily calorie summary",
        description=(
            "Returns total calories, protein, fats, and carbohydrates for the authenticated user "
            "on a specific date. Pass `date` in YYYY-MM-DD format as a query parameter. "
            "If not provided, defaults to today."
        ),

        responses={
            200: {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "format": "date"},
                    "total_calories": {"type": "integer"},
                    "total_protein": {"type": "integer"},
                    "total_fats": {"type": "integer"},
                    "total_carbohydrates": {"type": "integer"},
                }
            },
            401: {"description": "Unauthorized — user must be authenticated"},
        },
    )
)

class DailyCaloriesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        target_date = request.GET.get("date")
        if not target_date:
            target_date = date.today()

        meals = Nutrition.objects.filter(
            user=request.user,
            date=target_date
        ).aggregate(
            total=Sum('calories'),
            total_protein = Sum('protein'),
            total_fats = Sum('fats'),
            total_carbs = Sum('carbohydrates')
        )

        return Response({
                "date": str(target_date),
                "total_calories": meals["total"] or 0,
                "total_protein": meals["total_protein"] or 0,
                "total_fats": meals["total_fats"] or 0,
                "total_carbohydrates": meals["total_carbs"] or 0
            }
        )