from django.shortcuts import render
from django.http import HttpResponse
from app.models import Pais
from app.models import Continente
from app.models import Idioma
from app.forms import PaisFormulario
from app.forms import ContinenteFormulario
from app.forms import IdiomaFormulario

# Create your views here.

def inicio (request):
    return render(request, 'app/index.html')

def paises (request):
    return render(request, 'app/agregar_pais.html')

def buscar_pais(request):
    
    return render(request, 'app/busqueda_paises.html')

def resultados_busqueda_paises(request):
    nombre_pais = request.GET['nombre_pais']

    paises = Pais.objects.filter(nombre_pais__icontains=nombre_pais)
    return render(request, 'app/resultados_busquedas_paises.html', {"paises": paises})

def creacion_pais(request):
    
    if request.method == 'POST':
        formulario = PaisFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            pais = Pais(nombre_pais=data['nombre_pais'], num_habitantes=data['numero_habitantes'])
            pais.save()
        return render(request, 'app/index.html')
    else:
        formulario = PaisFormulario()
    
    contexto = {"formulario":formulario}
    return render(request, 'app/agregar_pais.html', contexto)

def continentes (request):
    return render(request, 'app/agregar_continente.html')

def creacion_continente(request):
    
    if request.method == 'POST':
        formulario = ContinenteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            continente = Continente(nombre_continente=data['nombre_continente'], nivel_economia=data['nivel_economia'])
            continente.save()
        return render(request, 'app/index.html')
    else:
        formulario = ContinenteFormulario()
    
    contexto = {"formulario":formulario}
    return render(request, 'app/agregar_continente.html', contexto)

def idiomas (request):
    return render(request, 'app/agregar_idioma.html')

def creacion_idioma(request):

    if request.method == 'POST':
        formulario = IdiomaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            idioma = Idioma(nombre_idioma=data['nombre_idioma'], origen_idioma=data['origen_idioma'])
            idioma.save()
        return render(request, 'app/index.html')
    else:
        formulario = IdiomaFormulario()
    
    contexto = {"formulario":formulario}
    return render(request, 'app/agregar_idioma.html', contexto)