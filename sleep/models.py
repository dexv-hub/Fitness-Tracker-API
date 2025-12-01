from django.db import models
from django.conf import settings

class Sleep(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()
    duration_hours = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.duration_hours and self.start_time and self.end_time:
            delta = self.end_time - self.start_time
            self.duration_hours = delta.total_seconds() / 3600
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.duration_hours}h on {self.date}"
