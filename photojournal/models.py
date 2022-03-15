from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='static/imgs/posts', default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_like')
    message = models.TextField(default=True)
    publication = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(null=True, default=False)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.message)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(default=True)
    publication = models.DateTimeField()

    def __str__(self):
        return str(self.text)


