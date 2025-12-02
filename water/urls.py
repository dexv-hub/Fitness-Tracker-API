from django.urls import path
from .views import WaterListCreateView, WaterDetailView

urlpatterns = [
    path("", WaterListCreateView.as_view(), name="water-list-create"),
    path("<int:pk>/", WaterDetailView.as_view(), name="water-detail"),
]