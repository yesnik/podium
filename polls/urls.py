from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll
from polls.views import PollView, PollDetailView, PollResultsView

urlpatterns = patterns('',

    #Указываем класс как представление
    url(r'^$',PollView.as_view()),
            
    url(r'^(?P<pk>\d+)/$', PollDetailView.as_view()),
            
    url(r'^(?P<pk>\d+)/results/$', PollResultsView.as_view(), name='poll_results'),
        
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)

'''
urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
'''