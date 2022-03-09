from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/imgs/avatar')
    info = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)
