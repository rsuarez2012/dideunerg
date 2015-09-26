from django.shortcuts import render_to_response
from django.template import RequestContext
from dideunerg.apps.deportes.models import Atletas, Entrenadores
from dideunerg.apps.home.forms import ContactForm, LoginForm, EditarAtletaForm, EditarEntrenadorForm
#from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger

#definimos la vista index
def index_view(request):
    return render_to_response('home/index.html',context_instance=RequestContext(request))

#definimos la vista de los entrenadores
def entrenadores_view(request,pagina):
    entrenadores = Entrenadores.objects.all()
    paginator = Paginator(entrenadores,1)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        entrenadores = paginator.page(page)
    except (EmptyPage,InvalidPage):
        entrenadores = paginator.page(paginator.num_pages)
    #print entrenadores
    ctx={'entrenadores':entrenadores}
    #ctx.update({'entrenadores':entrenadores})
    return render_to_response('home/entrenadores.html',ctx,context_instance=RequestContext(request))

#definimos los atletas
def atletas_view(request,pagina):
    atletas = Atletas.objects.all()
    paginator = Paginator(atletas,3)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        atletas = paginator.page(page)
    except (EmptyPage,InvalidPage):
        atletas = paginator.page(paginator.num_pages)
    #print entrenadores
    ctx={'atletas':atletas}
    #print atletas
    #ctx = {'lis_atletas':lis_atletas}
    #ctx.update({'atletas':atletas})
    return render_to_response('home/atletas.html',ctx,context_instance=RequestContext(request))
'''def borrar(request,id_atle):
    a = Atletas.objects.get(id=id_atle)
    a.delete()
    #ctx{'atletas':a}
    return render_to_response('home/eliminar.html',context_instance=RequestContext(request))'''


def singleAtleta_view(request,id_atle):
    prod = Atletas.objects.get(id=id_atle)
    ctx = {'atletas':prod}
    return render_to_response('home/singleAtleta.html',ctx,context_instance=RequestContext(request))

def singleEntrenador_view(request,id_entre):
    entre = Entrenadores.objects.get(id=id_entre)
    ctx = {'entrenadores':entre}
    return render_to_response('home/singleEntrena.html',ctx,context_instance=RequestContext(request))

def editarAtleta_view(request,id_atle):
    mes = Atletas.objects.get(pk=id_atle)
    if request.method=='POST':
        form = EditarAtletaForm(request.POST, instance=mes)
        if form.is_valid():
            form.save() 
            transaction.commit_unless_managed()
            return HttpResponseRedirect('/atletas/')           
    else:
        form = EditarAtletaForm(instance=mes)
    data = {
        'form': form,
    }
    return render_to_response("home/editarAtleta.html", data, context_instance=RequestContext(request))

def editarEntrenador_view(request,id_entre):
    var = Entrenadores.objects.get(pk=id_entre)
    if request.method=='POST':
        form = EditarEntrenadorForm(request.POST, instance=var)
        if form.is_valid():
            form.save() 
            transaction.commit_unless_managed()
            return HttpResponseRedirect('/entrenadores/')           
    else:
        form = EditarEntrenadorForm(instance=var)
    data = {
        'form': form,
    }
    return render_to_response("home/editarEntrena.html", data, context_instance=RequestContext(request))
    '''diccionario = {}
    diccionario.update(csrf(request))
    form = EditarAtletaForm()
    import pdb
    if request.method == 'POST':
        diccionario.update({'formulario':form})
        if form.is_valid():
            cedula = request.POST['cedula']
            p_nombre = request.POST['primer_nombre']
            s_nombre = request.POST['segundo_nombre']
            p_apellido = request.POST['primer_apellido']
            s_apellido = request.POST['segundo_apellido']
            sexo = request.POST['sexo']
            email = request.POST['email']
            tlf = request.POST['tlf']
            persona = Personas.objects.create(cedula=cedula,primer_nombre=p_nombre,segundo_nombre=s_nombre,primer_apellido=p_apellido,segundo_apellido=s_apellido, sexo=sexo, email=email, tlf=tlf)
            mensaje = "Guardado exitosamente"
            diccionario.update({'mensaje':mensaje})
            return render_to_response('formulario_personas.html', diccionario)
        else:
            mensaje = "Formulario incorrectamente llenado"
            diccionario.update({'mensaje':mensaje})
            return render_to_response('formulario_personas.html', diccionario)
    else:
        diccionario.update({'formulario':form})
        mensaje = "Bienvenido."
        diccionario.update({'mensaje':mensaje})
        return render_to_response('formulario_personas.html', diccionario)'''
    #return render_to_response('home/editarAtleta.html',context_instance=RequestContext(request))

def login_view(request):
    mensaje =""
    if  request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method =="POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "Usuario y/o password son Incorrectos"
        form = LoginForm()
        ctx ={'form':form,'mensaje':mensaje}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
