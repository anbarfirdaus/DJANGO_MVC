from django.contrib import admin
from .models import Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,LiveCode

# Register your models here.

my_model = [Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,LiveCode]
admin.site.register(my_model)