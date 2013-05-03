from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateTimeField()

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateTimeField()
