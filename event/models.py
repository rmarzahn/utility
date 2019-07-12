from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now = False, auto_now_add = False, default=timezone.now, help_text = 'Format: tt.mm.jjjj')
    time = models.TimeField(auto_now = False, auto_now_add = False, default=timezone.now, help_text = 'Format: --:--')
    street_number = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
