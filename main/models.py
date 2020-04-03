from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Image(models.Model):
    description = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, blank=True)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')


class Comment(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='SOME STRING')
    content = models.CharField(max_length=100)
