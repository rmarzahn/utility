from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'event/$', views.event_list, name="event_list"),
    url(r'event/create/$', views.event_create, name="event_create"),
]