from django.db.models import CharField
from django.db.models import TextField
from django.db.models import FileField
from django.db import models as models
from django.db.models import ImageField

# Create your models here.

class Mentee(models.Model):
    name = models.CharField(max_length=100)
    quotes = models.TextField()
    model_pic = models.FileField(upload_to='static/img/')
    
    def __str__(self):
        return self.name