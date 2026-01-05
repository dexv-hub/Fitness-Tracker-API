from django.core.cache import cache
from django.db.models import Sum
from nutrition.models import Nutrition

CACHE_TTL = 60 * 5

def get_daily_calories(user, target_date):
    cache_key = f"daily_calories:{user.id}:{target_date}"

    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    meals = Nutrition.objects.filter(
        user=user,
        date=target_date
    ).aggregate(
        total=Sum("calories"),
        total_protein=Sum("protein"),
        total_fats=Sum("fats"),
        total_carbs=Sum("carbohydrates"),
    )

    data = {
        "date": str(target_date),
        "total_calories": meals["total"] or 0,
        "total_protein": meals["total_protein"] or 0,
        "total_fats": meals["total_fats"] or 0,
        "total_carbohydrates": meals["total_carbs"] or 0,
    }

    cache.set(cache_key, data, CACHE_TTL)

    return data