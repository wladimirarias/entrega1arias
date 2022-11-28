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
    username = forms.CharField(label="Usuario")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo Electrónico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirme el Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ["email", "last_name", "first_name"]
        help_texts = {"email": "Indica un correo electrónico que uses habitualmente", "first_name": "", "last_name": "", "password1": ""}

class AvatarForm(forms.Form):
    imagen = forms.ImageField()