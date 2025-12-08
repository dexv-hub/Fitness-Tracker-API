from django.urls import path
from .views import DailyCaloriesView

urlpatterns = [
    path("calories/", DailyCaloriesView.as_view())
]