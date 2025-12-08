from django.urls import path
from .views import NutritionListCreateView, NutritionDetailView

urlpatterns = [
    path("", NutritionListCreateView.as_view(), name='nutrition-list-create'),
    path("<int:pk>/", NutritionDetailView.as_view(), name="nutrition-detail")
]