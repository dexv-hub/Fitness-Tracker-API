from django.urls import path
from .views import DailyCaloriesView

urlpatterns = [
    path("total_calories/", DailyCaloriesView.as_view())
]