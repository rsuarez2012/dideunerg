from django import forms
#from dideunerg.apps.deportes.modesl import Atletas
#from django.forms import Form, CharField, ModelForm
#from dideunerg.apps.deportes.models import Entrenadores

class addAtletaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    cedula = forms.IntegerField(widget=forms.TextInput())
    telefono = forms.IntegerField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.Textarea())
    cohorte = forms.IntegerField(widget=forms.TextInput())
    foto = forms.ImageField(required=False)
    def clean(self):
        return self.cleaned_data

'''class EntrenadoresForm(ModelForm):
    class Meta:
        model = Entrenadores'''
class entrenadoresForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    cedula = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    #disciplina = forms.ForeignKey('Disciplina')
    telefono = forms.CharField(widget=forms.TextInput())
    horas = forms.CharField(widget=forms.TextInput())
    lugar_de_entrenamiento = forms.CharField(widget=forms.TextInput())

    def clean(self):
        return self.cleaned_data

'''class editarAtletaForm(forms.ModelForm):
    class Meta:
        model = Editar'''
class editarAtletaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    cedula = forms.IntegerField(widget=forms.TextInput())
    telefono = forms.IntegerField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.Textarea())
    cohorte = forms.IntegerField(widget=forms.TextInput())
    foto = forms.ImageField(required=False)
    def clean(self):
        return self.cleaned_data
