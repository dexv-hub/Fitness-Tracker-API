from django.db import models
from django.conf import settings

class Workouts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=20)
    duration = models.PositiveIntegerField()
    burned_calories = models.FloatField()

    def __str__(self):
        return f"{self.user.email} - {self.workout_type}"