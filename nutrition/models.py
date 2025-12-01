from django.db import models
from django.conf import settings

class Nutrition(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calories = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user.email} - calories - {self.calories}, "
                f"carbohydrates - {self.carbohydrates}, "
                f"protein - {self.protein}, "
                f"fats - {self.fats}")