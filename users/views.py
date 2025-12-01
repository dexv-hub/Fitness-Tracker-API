
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import RegisterSerializers
from .models import User
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]
