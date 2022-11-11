from django import forms

class PaisFormulario(forms.Form):
    nombre_pais = forms.CharField()
    numero_habitantes = forms.IntegerField()

class ContinenteFormulario(forms.Form):
    nombre_continente = forms.CharField()
    nivel_economia = forms.CharField()

class IdiomaFormulario(forms.Form):
    nombre_idioma = forms.CharField()
    origen_idioma = forms.CharField()