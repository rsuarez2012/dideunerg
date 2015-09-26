from django import forms
from dideunerg.apps.deportes.models import Atletas, Entrenadores

class ContactForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput())
    Titulo = forms.CharField(widget=forms.TextInput())
    Texto = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

'''class editarAtletaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    apellido = forms.CharField(widget=forms.TextInput())
    cedula = forms.IntegerField(widget=forms.TextInput())
    telefono = forms.IntegerField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.Textarea())
    cohorte = forms.IntegerField(widget=forms.TextInput())
    foto = forms.ImageField(required=False)
    def clean(self):
        return self.cleaned_data'''

class EditarAtletaForm(forms.ModelForm):
    class Meta:
        model = Atletas

class EditarEntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenadores
