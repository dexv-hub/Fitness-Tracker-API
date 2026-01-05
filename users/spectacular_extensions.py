from drf_spectacular.extensions import OpenApiAuthenticationExtension
from users.authentication import RedisJWTAuthentication

class RedisJWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'users.authentication.RedisJWTAuthentication'
    name = 'RedisJWT'