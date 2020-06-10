from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import hashlib
import random
import sys


# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()


def create_session_hash():
    hash = hashlib.sha1()
    hash.update(str(random.randint(0, sys.maxsize)).encode('utf-8'))
    return hash.hexdigest()


class Questionnaire(models.Model):
    # Operational
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    nilai_choices = (
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1),
    )
    # Stage 1 fields
    nilai_satu = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_satu = models.TextField(blank=True)
    rekomendasi_satu = models.TextField(blank=True)
    nilai_dua = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_dua = models.TextField(blank=True)
    rekomendasi_dua = models.TextField(blank=True)
    # Stage 2 fields
    nilai_tiga = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_tiga = models.TextField(blank=True)
    rekomendasi_tiga = models.TextField(blank=True)
    nilai_empat = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_empat = models.TextField(blank=True)
    rekomendasi_empat = models.TextField(blank=True)
    # Stage 3 fields
    nilai_lima = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_lima = models.TextField(blank=True)
    rekomendasi_lima = models.TextField(blank=True)
    nilai_enam = models.IntegerField(choices=nilai_choices, default=4)
    keterangan_enam = models.TextField(blank=True)
    rekomendasi_enam = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})
