from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'visualweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'^upload/', include('upload.urls', namespace='upload')),
    url(r'^poll/', include('poll.urls', namespace='poll')),
    url(r'^algorithm/', include('algorithm.urls', namespace='algorithm')),
    url(r'^poj/', include('poj.urls', namespace='poj')),
    url(r'^admin/', include(admin.site.urls)),
]
