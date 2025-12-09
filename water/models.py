from django.db import models
from datetime import date
from django.conf import settings

class Water(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    water_consumption = models.FloatField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return f"{self.user.email} - {self.water_consumption} ml"