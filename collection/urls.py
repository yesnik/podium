from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from collection.models import Collection, Author, Vuz, Nomination, Prizer
from collection.views import CollectionVuzListView, AuthorDetailView, CollectionNominationListView, PrizerLastYearListView

urlpatterns = patterns('',

    #/collection/
    url(r'^$', ListView.as_view(
        queryset=Collection.objects.all(),
        context_object_name='collection_list',
        template_name='collection/collection_list.html'),
        name="collection_list"),

    #/collection/vuz
    url(r'^vuz/$', ListView.as_view(
        queryset=Vuz.objects.all(),
        context_object_name='vuz_list',
        template_name='collection/vuz_list.html'),
        name="vuz_list"),

    #/collection/vuz/vuz_url
    url(r'^vuz/(?P<vuz>[a-zA-Z]+)/$', CollectionVuzListView.as_view(),
        name="vuz_collections"),

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

    #/collection/prizers
    url(r'^prizers/$', PrizerLastYearListView.as_view()),
        

)