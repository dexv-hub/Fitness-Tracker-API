from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from datetime import date
from nutrition.models import Nutrition
from django.db.models import Sum

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