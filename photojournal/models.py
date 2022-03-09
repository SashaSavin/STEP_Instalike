from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='static/imgs/posts', default=True)
    likes = models.ManyToManyField(User, related_name='post_like')
    message = models.TextField(default=True)
    publication = models.DateTimeField()
    slug = models.SlugField(null=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.message)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(default=True)
    publication = models.DateTimeField()

    def __str__(self):
        return str(self.text)
