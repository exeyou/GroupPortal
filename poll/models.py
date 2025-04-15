from django.db import models
from accounts.models import User

class Poll(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)