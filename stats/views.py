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
        ).aggregate(total=Sum('calories'))

        return Response({
                "date": str(target_date),
                "total_calories": meals["total"] or 0
            }
        )