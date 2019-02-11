from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone
from django.db import models as models

# Create your models here.

class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    bidang = models.CharField(max_length=100)
    jadwal_praktek = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama
         
class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=255)
    alamat = models.CharField (max_length=255)
    keluhan = models.CharField (max_length=255)

class Resep(models.Model):
    nama = models.CharField(max_length=100)
    total_harga = models.CharField(max_length=100)
    kumpulan_obat = models.CharField(max_length=100)

class Obat (models.Model):
    nama = models.CharField(max_length=100)
    kandungan = models.CharField(max_length=100)
    khasiat = models.CharField (max_length=100)
