from django.db import models
from django.contrib.auth.models import User

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Учень
    subject = models.CharField(max_length=100)                   # Предмет
    grade = models.IntegerField()                                # Оцінка
    date = models.DateField(auto_now_add=True)                   # Дата оцінки

    def __str__(self):
        return f"{self.student.username} - {self.subject}: {self.grade}"