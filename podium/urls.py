# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from podium.views import PageView, VuzYearListView
from django.views.generic import DetailView, ListView
from collection.models import Collection, Author, Vuz
from collection.views import CollectionVuzListView, CollectionYearVuzListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', PageView.as_view()),
    url(r'^page/', include('page.urls')),
    url(r'^collection/', include('collection.urls')),

    #/vuz/
    url(r'^vuz/$', VuzYearListView.as_view(),
        name="vuz_year_list"),

    #vuz/all
    url(r'^vuz/all/$', ListView.as_view(
        queryset=Vuz.objects.all(),
        context_object_name='vuz_list',
        template_name='collection/vuz_list.html'),
        name="vuz_list"),



    #/vuz/2013   
    url(r'^vuz/(?P<year>\d{4})/$', VuzYearListView.as_view(),
        name="vuz_year_list"),

    #/vuz/2013/vuz_url
    url(r'^vuz/(?P<year>\d{4})/(?P<vuz>[a-zA-Z]+)/$', CollectionYearVuzListView.as_view(),
        name="year_vuz_collections"),

    # vuz/vuz_url
    url(r'^vuz/(?P<vuz>[a-zA-Z]+)/$', CollectionVuzListView.as_view(),
        name="vuz_collections"),

    url(r'', include('contest.urls')),

    # Setting for application 'attachments' for serving files
    url(r'^'+settings.MEDIA_ROOT+'attachments/', include('attachments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # Устанавливаем настройки для обработки картинок, загруженных пользователем
    urlpatterns += patterns('',
        (r'^' + settings.MEDIA_ROOT + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )