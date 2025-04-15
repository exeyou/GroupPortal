from django.db import models
from accounts.models import User

class Gallery(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="gallery", on_delete=models.CASCADE)
    media = models.FileField(blank=True, null=True)
    approval = models.BooleanField(default=True)