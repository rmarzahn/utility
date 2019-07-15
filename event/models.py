from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now = False, auto_now_add = False, default=timezone.now, verbose_name = 'Date Format (tt.mm.jjjj)')
    time = models.TimeField(auto_now = False, auto_now_add = False, default=timezone.now, verbose_name = 'Time Format (--:--)')
    street_number = models.CharField(max_length=50, verbose_name = 'Street and Number')
    postalcode = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

