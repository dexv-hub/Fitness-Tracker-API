from django.db import models
from django.conf import settings
import datetime

class Workouts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=20)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    burned_calories = models.FloatField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.user.email} - {self.workout_type}"