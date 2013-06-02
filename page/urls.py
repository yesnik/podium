# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from page.views import PageDetailView


urlpatterns = patterns('',

    url(r'nik/$', PageDetailView.as_view()),
    url(r'(?P<page_url>\w+)/$', PageDetailView.as_view()),
)