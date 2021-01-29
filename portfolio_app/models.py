from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  content = models.TextField()
