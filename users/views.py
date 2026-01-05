from rest_framework import generics, status, serializers
from .serializers import RegisterSerializers
from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .jwt_blacklist import blacklist_token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]

class LogoutSerializer(serializers.Serializer):
    pass

class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh = request.data.get("refresh")
        token = RefreshToken(refresh)

        blacklist_token(
            token["jti"],
            token["exp"] - token.current_time.timestamp()
        )

        return Response({"detail": "Logged out"})
