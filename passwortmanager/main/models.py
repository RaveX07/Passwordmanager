from django.db import models

# Create your models here.
class Password(models.Model):
    WebsiteURL = models.CharField(max_length=100)
    Passwort = models.CharField(max_length=50)
    WebsiteName = models.CharField(max_length=32)
    Benutzer = models.CharField(max_length=50)

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Passwort = models.CharField(max_length=50)