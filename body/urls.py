from django.urls import path
from .views import BodyListCreateView, BodyDetailView

urlpatterns = [
    path("", BodyListCreateView.as_view(), name="body-list-create"),
    path("<int:pk>/", BodyDetailView.as_view(), name="body-detail")
]