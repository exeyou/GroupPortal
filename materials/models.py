from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)  # Для хранения текста с ссылками
    media = models.FileField(upload_to='materials/', blank=True, null=True)  # Для файлов (видео, изображения)
    youtube_video_id = models.CharField(max_length=255, blank=True, null=True)  # Для YouTube видео
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

admin.site.register(Material)