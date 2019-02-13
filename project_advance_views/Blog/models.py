from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import FileField
from django.db.models import DateTimeField
from django.utils import timezone
from django.db import models as models


# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField()
    model_pic = models.FileField(upload_to='static/img/')
    
    def __str__(self):
        return self.Title
