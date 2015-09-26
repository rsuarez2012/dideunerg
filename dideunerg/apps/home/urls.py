from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('dideunerg.apps.home.views',
    url(r'^$','index_view',name='vista_principal'),
    #url(r'^atletas/$','atletas_view',name='vista_atletas'),
    #url(r'^entrenadores/$', 'entrenadores_view'),
    url(r'^entrenadores/page/(?P<pagina>.*)/$','entrenadores_view'),
    #url(r'^add/atletas/$','add_atletas_view'),
    #url(r'^about/$','about_view',name='vista_about'),
    url(r'^atletas/page/(?P<pagina>.*)/$','atletas_view',name='vista_atletas'),
    url(r'^atleta/(?P<id_atle>.*)/$','singleAtleta_view',name='vista_single_atleta'),
    url(r'^entrenador/(?P<id_entre>.*)/$','singleEntrenador_view'),
    url(r'^editar/atleta/(?P<id_atle>.*)/$','editarAtleta_view',name='vista_single_atleta'),
    url(r'^editar/entrenador/(?P<id_entre>.*)/$','editarEntrenador_view'),
    #url(r'^contacto/$','contacto_view',name='vista_contactos'),
    url(r'^login/$','login_view',name='vista_login'),
    url(r'^logout/$','logout_view',name='vista_logout'),

)
