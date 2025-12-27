from django.db import models
import datetime
from django.conf import settings

class Water(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    water_consumption = models.FloatField()
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.user.email} - {self.water_consumption} ml"