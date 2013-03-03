from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from persons.models import *
from persons.views import *

urlpatterns = patterns('',

    url(r'^contacts/$',ListView.as_view(
        queryset=Person.objects.all(),
        context_object_name='persons',
        template_name='persons/persons_list.html'
    )),
    
    url(r'^zhuri/$',ListView.as_view(
        queryset=Zhuri.objects.all(),
        context_object_name='zhuri_list',
        template_name='persons/zhuri_list.html'
    )),
            
    #url(r'^(?P<pk>\d+)/$', PageView.as_view()),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
        model=Page,
        context_object_name='page',
        template_name='blog/blog_detail.html'
    )),

)