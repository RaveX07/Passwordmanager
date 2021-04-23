from django.db import models

# Create your models here.
class Password(models.Model):
    websiteURL = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    websiteName = models.CharField(max_length=32)
    user = models.CharField(max_length=50)

class User(models.Model):
    Name = models.CharField(max_length=50)
    EMail = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)