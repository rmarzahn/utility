from django.shortcuts import render, redirect
from .models import Event
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
import datetime

# Create your views here.

def event_list(request):
    events = Event.objects.all().order_by('date').order_by('time').filter(date__gte=datetime.date.today())
    return render(request, 'event/event_list.html', {'events': events})


@login_required()
def event_create(request):
    if request.method == 'POST':
        form = forms.CreateEvent(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()            
            return redirect('event_list')
    else:
        form = forms.CreateEvent()
    return render(request, 'event/event_create.html', {'form':form})


