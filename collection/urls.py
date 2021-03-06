﻿# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from collection.models import Collection, Author, Vuz, Nomination, Prizer
from collection.views import CollectionVuzListView, AuthorDetailView, \
    CollectionNominationListView, PrizerLastYearListView, PrizerYearListView, \
    CollectionYearListView

urlpatterns = patterns('',

    #/collection/
    url(r'^$', CollectionYearListView.as_view(show_active_year=True),
        name="collection_list"),

    #/collection/2012
    url(r'^(?P<year>\d{4})/$', CollectionYearListView.as_view(), 
        name="collection_year_list"),



    #/collection/nomination/ 
    url(r'^nomination/$', ListView.as_view(
        queryset=Nomination.objects.all(),
        context_object_name='nomination_list',
        template_name='collection/nomination_list.html'),
        name="nomination_list"),

    #/collection/nomination/nomination_url
    url(r'^nomination/(?P<nomination_url>[a-zA-Z_]+)/$', CollectionNominationListView.as_view(),
        name="nomination_collections"),

    #/collection/122   
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
        model=Collection,
        template_name='collection/collection_detail.html'),
        name="collection_detail"),

    #/author/ 
    url(r'^author/$', ListView.as_view(
        queryset=Author.objects.all(),
        context_object_name='author_list',
        template_name='collection/author_list.html'),
        name="author_list"),

    #/author/122   
    url(r'^author/(?P<pk>\d+)/$',
        AuthorDetailView.as_view(),
        name="author_detail"),

)