from django.db import models
from django.utils import timezone

from blog.models import Post
from users.models import User
# Create your models here.

class Comment(models.Model):
    comment = models.TextField(null=True)
    data_comment = models.TimeField(default =timezone.now)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return self.comment

    