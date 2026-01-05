from django.core.cache import cache

BLACKLIST_PREFIX = "jwt:blacklist:"

def blacklist_token(jti, exp):
    cache.set(f"{BLACKLIST_PREFIX}{jti}", "1", timeout=exp)

def is_token_blacklisted(jti):
    return cache.get(f"{BLACKLIST_PREFIX}{jti}") is not None
