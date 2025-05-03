from email.policy import default

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class PortfolioProject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    screenshot = models.ImageField(upload_to='projects/screenshots/', blank=True, null=True)
    link = models.URLField(blank=True, default = "не вказано")
    file = models.FileField(upload_to='projects/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Учень
    subject = models.CharField(max_length=100)                   # Предмет
    grade = models.IntegerField()                                # Оцінка
    date = models.DateField(auto_now_add=True)                   # Дата оцінки

    def __str__(self):
        return f"{self.student.username} - {self.subject}: {self.grade}"