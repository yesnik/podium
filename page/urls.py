from django.conf.urls import patterns, include, url
from page.views import PageDetailView


urlpatterns = patterns('',

    url(r'^nik/$', PageDetailView.as_view()),
    url(r'^(?P<pk>\d+)/$', PageDetailView.as_view()),
)