from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    num = models.IntegerField()
    score = models.IntegerField()