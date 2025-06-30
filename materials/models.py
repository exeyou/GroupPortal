from django.db import models
from django.contrib.auth.models import User
from config.utils import extract_youtube_video_id

class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to='materials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def youtube_video_id(self):
        return extract_youtube_video_id(self.content or '')
