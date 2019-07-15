from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateEvent(forms.ModelForm):
    date = forms.DateField(widget=DateInput, label = 'Date (Format: tt.mm.jjjj)')
    time = forms.TimeField(widget=TimeInput, label = 'Time (Format: --:--)')
    class Meta:
        model = models.Event
        fields = ['title', 'text', 'date', 'time', 'street_number', 'postalcode', 'city']


