from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from .jwt_blacklist import is_token_blacklisted

class RedisJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        validated_token = super().get_validated_token(raw_token)

        jti = validated_token.get("jti")
        if jti and is_token_blacklisted(jti):
            raise InvalidToken("Token is blacklisted")

        return validated_token
