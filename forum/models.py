from django.db import models
from accounts.models import User
from django.contrib import admin

class Branch(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="branches")

    def __str__(self):
        return self.title


class Comment(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(blank=True, null=True)




class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comments")
    created_at = models.DateTimeField(auto_now_add=True)


admin.site.register(Branch)
admin.site.register(Comment)
admin.site.register(Like)