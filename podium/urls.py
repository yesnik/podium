from django.conf.urls import patterns, include, url
from django.conf import settings
from podium.views import PageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', PageView.as_view()),
    url(r'^page/', include('page.urls')),
    url(r'^collection/', include('collection.urls')),
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