#!/usr/bin/env python
# encoding: utf-8


from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
        url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
        url(r'^base/$', views.base, name='base'),
        url(r'^list/$', views.listing, name="listing"),
        ]
