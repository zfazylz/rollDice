from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.CharField(max_length=50, default='NONE')
    name = models.CharField(max_length=50, default='NONE')
    password = models.CharField(max_length=50, default='NONE')
    balance = models.IntegerField(default=0)
