from django.db import models
from django.conf import settings
import datetime

class Nutrition(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calories = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.user.email} - {self.calories}"
