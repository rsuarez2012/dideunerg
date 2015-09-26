from django.contrib import admin
from dideunerg.apps.deportes.models import Entrenadores, Atletas
class AtletasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'telefono', 'direccion', 'cohorte')

admin.site.register(Entrenadores)
#admin.site.register(Disciplina)
#admin.site.register(Nucleos)
#admin.site.register(Carreras)
#admin.site.register(Recor_Del_Atleta)
admin.site.register(Atletas, AtletasAdmin)
