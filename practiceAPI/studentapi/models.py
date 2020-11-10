from django.db import models

# Create your models here.
class Biodata(models.Model):
    nickname = models.CharField(max_length = 50, null = True)
    fullname = models.CharField(max_length = 100, null = True)
    randomThought = models.CharField(max_length = 200, null = True)