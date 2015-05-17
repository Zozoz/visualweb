#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.show, name='show'),
        url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
        ]
