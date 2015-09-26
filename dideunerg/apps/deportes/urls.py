from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('dideunerg.apps.deportes.views',
    url(r'^add/atletas/$','add_atletas'),
    url(r'^agregar/$','agregar'),
    url(r'^eliminar/(?P<id_atle>.*)/$','borrar'),
    url(r'^elimi/(?P<id_entre>.*)/$','borrar_entrenador'),

)
