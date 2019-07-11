from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^classics/$', views.classics, name='classics'),
    url(r'^blog/$', views.post_list, name='blog'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.post_category, name='post_category'),
]

urlpatterns += staticfiles_urlpatterns()

