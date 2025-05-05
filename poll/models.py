# models.py
from django.db import models
from accounts.models import User

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=50, choices=[
        ('text', 'Text'),
        ('radio', 'Single Choice'),
        ('checkbox', 'Multiple Choice'),
    ])
    order = models.PositiveIntegerField(default=1)  # NEW: Defines question order inside the survey

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class SurveyResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'survey')

class Answer(models.Model):
    result = models.ForeignKey(SurveyResult, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text_answer = models.TextField(blank=True, null=True)
    choices = models.ManyToManyField(Choice, blank=True)
