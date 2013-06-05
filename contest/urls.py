# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from contest.models import Jury, Organisator
from contest.models import Winner
from contest.views import JuryContestListView, JuryYearsListView, SponsorYearsListView


urlpatterns = patterns('',

    url(r'^jury/$', JuryYearsListView.as_view(),
        name="jury_list"),

    #/jury/2012
    url(r'^jury/(?P<year>\d{4})/$', JuryContestListView.as_view(),
        name="jury_year_list"),

    #/jury/1
    url(r'^jury/(?P<pk>\d+)/$', DetailView.as_view(
        model=Jury,
        template_name="jury_detail.html",
        context_object_name='jury'),
        name="jury_detail"),

    #/sponsor/
    url(r'^sponsor/$', SponsorYearsListView.as_view(),
        name="sponsor_list"),

    #/organisators/
    url(r'^organisators/$', ListView.as_view(
        model=Organisator,
        template_name="organisator_list.html",
        context_object_name='organisator_list'),
        name="organisator_list"),

    #/winner
    url(r'^winner/(?P<pk>\d+)$', DetailView.as_view(
        model=Winner,
        context_object_name='winner',
        template_name='contest/winner_detail.html'),
        name="winner_detail"),
)
