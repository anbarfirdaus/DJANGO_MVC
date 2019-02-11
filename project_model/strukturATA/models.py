from django.db.models import CharField
from django.db.models import TextField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.utils import timezone

from django.db import models as models

# Create your models here.

class Mata_pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=100)
    jadwal_dimulai = models.DateTimeField ()
    jadwal_berakhir = models.DateTimeField ()

    def __str__(self):
        return self.nama_pelajaran

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=25)
    jabatan = models.CharField(max_length=100)


class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=25)
    nomor_absen = models.CharField(max_length=10)
    nilai_rata_rata = models.CharField(max_length=10)

class Mentor (models.Model):
    nama_lengkap = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=25)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)



class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=100)
    banyak_soal = models.CharField(max_length=10)
    bobot_nilai = models.CharField(max_length=10)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)

class LiveCode (models.Model):
    nama_live_code = models.CharField(max_length=100)
    banyak_soal = models.CharField(max_length=10)
    bobot_nilai = models.CharField(max_length=10)
    tanggal_pelaksanaan = models.DateTimeField ()
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)





