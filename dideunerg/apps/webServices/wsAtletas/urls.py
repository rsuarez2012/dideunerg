from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('dideunerg.apps.webServices.wsAtletas.views',
    url(r'^ws/atletas/$','wsAtletas_view',name="ws_atletas_url"),

)
