from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import *
from blog.views import PageListView, PageView

urlpatterns = patterns('',

    #
    url(r'^$',PageListView.as_view()),
            
    url(r'^(?P<pk>\d+)/$', PageView.as_view()),
            
    #url(r'^(?P<pk>\d+)/results/$', PollResultsView.as_view(), name='poll_results'),
        
    #url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)