from django.urls import path
from .views import WorkoutsListCreateView, WorkoutsDetailView

urlpatterns = [
    path("", WorkoutsListCreateView.as_view(), name='workouts-list-create'),
    path("<int:pk>/", WorkoutsDetailView.as_view(), name="workouts-detail")
]