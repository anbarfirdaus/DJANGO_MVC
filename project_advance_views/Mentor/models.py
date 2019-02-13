from django.db import models as models
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import FileField
from django.db.models import ImageField

# Create your models here.

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    quotes = models.TextField(max_length=500)
    model_pic = models.FileField(upload_to='static/img/')
    def __str__(self):
        return self.name
