from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from admin_panel.models import AndroidApp


class CustomUser(AbstractUser):
    # Additional user profile fields
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    points_earned = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"




