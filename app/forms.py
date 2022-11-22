from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PaisFormulario(forms.Form):
    nombre_pais = forms.CharField()
    numero_habitantes = forms.IntegerField()

class ContinenteFormulario(forms.Form):
    nombre_continente = forms.CharField()
    nivel_economia = forms.CharField()

class IdiomaFormulario(forms.Form):
    nombre_idioma = forms.CharField()
    origen_idioma = forms.CharField()

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]