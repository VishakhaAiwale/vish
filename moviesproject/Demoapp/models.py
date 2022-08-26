from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate = models.DateField()
    mname = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    actress = models.CharField(max_length=50)
    ratings = models.IntegerField()
