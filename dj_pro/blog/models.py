from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    ID = models.IntegerField(max_length=10)
    real_name = models.TextField(max_length=20)
    country = models.TextField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


