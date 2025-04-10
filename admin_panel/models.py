from django.db import models

class AndroidApp(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    download_url = models.URLField()
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


