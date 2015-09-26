from django.shortcuts import render_to_response
from django.template import RequestContext
from dideunerg.apps.deportes.forms import addAtletaForm, entrenadoresForm, editarAtletaForm#, addEntrenadoresForm
from dideunerg.apps.deportes.models import Atletas, Entrenadores
from django.http import HttpResponseRedirect

def add_atletas(request):
    info = "Inicializando"
    if request.user.is_authenticated():
        if request.method == "POST":
            form = addAtletaForm(request.POST,request.FILES)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                apellido = form.cleaned_data['apellido']
                cedula = form.cleaned_data['cedula']
                telefono = form.cleaned_data['telefono']
                direccion = form.cleaned_data['direccion']
                cohorte = form.cleaned_data['cohorte']
                foto = form.cleaned_data['foto']
                p = Atletas()
                if foto:
                    p.foto = foto
                p.nombre = nombre
                p.apellido = apellido
                p.cedula = cedula
                p.telefono = telefono
                p.direccion = direccion
                p.cohorte = cohorte
                #p.status = True
                p.save() # Guardar la informacion
                info = "Se guardo satisfactoriamente!!!!!"
            else:
                info = "informacion con datos incorrectos"
        form = addAtletaForm()
        ctx = {'form':form, 'informacion':info}
        #return render_to_response('home/atletas.html',ctx,context_instance=RequestContext(request))
        return render_to_response('deportes/addAtleta.html',ctx,context_instance=RequestContext(request))
    else:
    #info = "iniciando"
        #form = addProductForm()
	#ctx = {'form':form}
        #return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
        return HttpResponseRedirect('/')

def agregar(request):
    info = "Inicializando"
    if request.user.is_authenticated():
        if request.method == "POST":
            form = entrenadoresForm(request.POST,request.FILES)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                apellido = form.cleaned_data['apellido']
                cedula = form.cleaned_data['cedula']
                telefono = form.cleaned_data['telefono']
                direccion = form.cleaned_data['direccion']
                horas = form.cleaned_data['horas']
                lugar_de_entrenamiento = form.cleaned_data['lugar_de_entrenamiento']
                p = Entrenadores()
                if horas:
                    p.horas = horas
                p.nombre = nombre
                p.apellido = apellido
                p.cedula = cedula
                p.telefono = telefono
                p.direccion = direccion
                p.lugar_de_entrenamiento = lugar_de_entrenamiento
                #p.status = True
                p.save() # Guardar la informacion
                info = "Se guardo satisfactoriamente!!!!!"
            else:
                info = "informacion con datos incorrectos"
        form = entrenadoresForm()
        ctx = {'form':form, 'informacion':info}
        #return render_to_response('home/atletas.html',ctx,context_instance=RequestContext(request))
        return render_to_response('deportes/addEntrenador.html',ctx,context_instance=RequestContext(request))
    else:
    #info = "iniciando"
        #form = addProductForm()
	#ctx = {'form':form}
        #return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
        return HttpResponseRedirect('/')

def borrar(request,id_atle):
    a = Atletas.objects.get(id=id_atle)
    a.delete()
    print a
    '''ctx{}
    ctx.update({'atletas':a})'''
    return render_to_response('deportes/eliminar.html',context_instance=RequestContext(request))

def borrar_entrenador(request,id_entre):
    b = Entrenadores.objects.get(id=id_entre)
    b.delete()
    print b
    return render_to_response('deportes/eliminarEntre.html',context_instance=RequestContext(request))
