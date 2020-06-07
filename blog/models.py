from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import hashlib
import random
import sys
from . import constants

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
    session_hash = models.CharField(max_length=40, unique=True, blank=True)
    stage = models.CharField(max_length=10, default=constants.STAGE_1,)
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

    hidden_fields = ['stage']
    required_fields = ['nilai_satu', 'keterangan_satu', 'rekomendasi_satu',
                       'nilai_dua', 'keterangan_dua', 'rekomendasi_dua',
                       'nilai_tiga', 'keterangan_tiga', 'rekomendasi_tiga',
                       'nilai_empat', 'keterangan_empat', 'rekomendasi_empat',
                       'nilai_lima', 'keterangan_lima', 'rekomendasi_lima',
                       'nilai_enam', 'keterangan_enam', 'rekomendasi_enam', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.session_hash:
            while True:
                session_hash = create_session_hash()
                if Questionnaire.objects.filter(session_hash=session_hash).count() == 0:
                    self.session_hash = session_hash
                    break

    @staticmethod
    def get_fields_by_stage(stage):
        fields = ['stage']
        if stage == constants.STAGE_1:
            fields.extend(['nilai_satu', 'keterangan_satu', 'rekomendasi_satu',
                           'nilai_dua', 'keterangan_dua', 'rekomendasi_dua', ])
        elif stage == constants.STAGE_2:
            fields.extend(['nilai_tiga', 'keterangan_tiga', 'rekomendasi_tiga',
                           'nilai_empat', 'keterangan_empat', 'rekomendasi_empat', ])
        elif stage == constants.STAGE_3:
            fields.extend(['nilai_lima', 'keterangan_lima', 'rekomendasi_lima',
                           'nilai_enam', 'keterangan_enam', 'rekomendasi_enam', ])
        return fields
