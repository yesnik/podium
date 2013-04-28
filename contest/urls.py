from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from contest.models import Jury
from contest.views import JuryContestListView, JuryYearsListView


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
)
