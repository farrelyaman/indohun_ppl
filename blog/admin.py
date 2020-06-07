from django.contrib import admin
from .models import (
    ContactUs,
    Questionnaire,
)

# Register your models here.

admin.site.register(ContactUs)
admin.site.register(Questionnaire)
