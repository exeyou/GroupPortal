# models.py
from django.db import models
from django.contrib import admin

class Event(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    media = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

admin.site.register(Event)