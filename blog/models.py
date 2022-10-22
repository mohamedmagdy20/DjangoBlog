from email.policy import default
from enum import auto
from pyexpat import model
from time import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
class Post(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.BigIntegerField(default=0)
    def __str__(self) :
        return self.title    

    def get_absolute_url  (self):
        return reverse('post_detail',kwargs={'pk':self.pk})