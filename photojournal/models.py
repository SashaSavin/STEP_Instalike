from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='static/imgs/posts', default=True)
    message = models.TextField(default=True)
    publication = models.DateTimeField()

    def __str__(self):
        return str(self.message)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(default=True)
    publication = models.DateTimeField()

    def __str__(self):
        return str(self.text)
