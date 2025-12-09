from django.db import models
from django.conf import settings
from datetime import date

class Body(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    date = models.DateField(default=date.today())

    def __str__(self):
        return f"{self.user.email} - {self.weight} kg"