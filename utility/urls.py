from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('event.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.post_list, name="home"),
    url(r'^blog/$', views.post_list, name='blog'),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^event/$', include('event.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)