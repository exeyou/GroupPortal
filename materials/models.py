from django.db import models
from accounts.models import User

class Materials(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
