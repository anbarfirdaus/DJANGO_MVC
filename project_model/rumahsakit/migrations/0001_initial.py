# Generated by Django 2.1.5 on 2019-02-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=255)),
                ('bidang', models.CharField(max_length=100)),
                ('jadwal_praktek', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kandungan', models.CharField(max_length=100)),
                ('khasiat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.TextField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('keluhan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('total_harga', models.CharField(max_length=100)),
                ('kumpulan_obat', models.CharField(max_length=100)),
            ],
        ),
    ]
