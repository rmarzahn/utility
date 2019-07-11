from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class CreateEvent(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    class Meta:
        model = models.Event
        fields = ['title', 'text', 'date', 'time', 'street_number', 'postalcode', 'city']


