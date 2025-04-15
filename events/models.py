from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(blank=True, null=True)