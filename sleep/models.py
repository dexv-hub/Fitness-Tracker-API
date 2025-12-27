from django.db import models
from django.conf import settings
import datetime

class Sleep(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_hours = models.FloatField()
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            self.duration_hours = round(delta.total_seconds() / 3600, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.duration_hours}h on {self.start_time.date()}"
