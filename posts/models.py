from users.models import User
from django.db import models

class Post(models.Model):
  body = models.CharField(max_length=10000)
  timestamp = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = "Posts"

class PostFile(models.Model):
  url = models.CharField(max_length=1000)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  class Meta:
    db_table = "PostFiles"

class Like(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  timestamp = models.FloatField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = "Likes"

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  body = models.CharField(max_length=5000)
  timestamp = models.FloatField()

  class Meta:
    db_table = "Comments"
