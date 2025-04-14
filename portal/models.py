from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to='message_images/', blank=True, null=True)

    def __str__(self):
        return f'{self.author.username} in {self.branch.name} at {self.created_at.strftime("%Y-%m-%d %H:%M")}'
