# Create your views here.
from django.http import HttpResponse
from dideunerg.apps.deportes.models import Atletas
#integramos la serializacion de los objetos
from django.core import serializers

def wsAtletas_view(request):
#	data = serializers.serialize("json",atletas.objects.filter(status=True))
	data = serializers.serialize("json",Atletas.objects.all())
	return HttpResponse(data,mimetype="application/json")
