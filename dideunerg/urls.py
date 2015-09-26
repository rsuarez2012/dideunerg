from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dideunerg.views.home', name='home'),
    # url(r'^dideunerg/', include('dideunerg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('dideunerg.apps.deportes.urls')),
    url(r'^',include('dideunerg.apps.home.urls')),
    url(r'^',include('dideunerg.apps.webServices.wsAtletas.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
