from django.contrib import admin
from .models import Mentee,BlogPost

# Register your models here.

my_model = [BlogPost,Mentee]
admin.site.register(my_model)
