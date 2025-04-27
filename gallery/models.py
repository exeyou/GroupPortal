from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media_uploads/')
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} by {self.user.username}"
