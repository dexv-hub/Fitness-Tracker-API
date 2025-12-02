from django.urls import path
from .views import SleepListCreateView, SleepDetailView

urlpatterns = [
    path("", SleepListCreateView.as_view(), name='sleep-create-list'),
    path("<int:pk>/", SleepDetailView.as_view(), name='sleep-detail')
]