from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone
from django.db import models as models

# Create your models here.

class Hewan (models.Model):
    nama = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    berat = models.CharField(max_length=10)
    umur = models.CharField(max_length=10)

class Kandang(models.Model):
    nama = models.CharField(max_length=100)
    isi_kandang = models.CharField(max_length=100)
    luas_kandang = models.CharField(max_length=100)

class Penjaga (models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=100)
    jadwal_jaga = models.CharField(max_length=100)

class Pengunjung (models.Model):
    nama = models.CharField(max_length=100)
    nomor_telepon = models.CharField(max_length=100)
    hari_berkunjung = models.CharField(max_length=100)