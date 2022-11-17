from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Pais, Continente, Idioma
from app.forms import PaisFormulario, ContinenteFormulario, IdiomaFormulario
from django.core.paginator import Paginator
from django.http import Http404
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

    paises = Pais.objects.all().order_by('nombre_pais')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(paises, 5)
        paises = paginator.page(page)
    except:
        raise Http404
    
    # contexto2 = {"paises":paises} **CÓDIGO ORIGINAL, SE CAMBIÓ POR PAGINADOR
    contexto2 = {"entity":paises, "paginator":paginator}
    contexto = {"formulario":formulario}

    nuevo_contexto = {**contexto, **contexto2}
    return render(request, 'app/agregar_pais.html', nuevo_contexto)

def edit_pais(request, id):
    pais = Pais.objects.get(id=id)

    if request.method == 'POST':
        formulario = PaisFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            pais.nombre_pais = data["nombre_pais"]
            pais.num_habitantes = data["numero_habitantes"]
            pais.save()
            return redirect(creacion_pais)
        else:
            return render(request, "app/editar_pais.html", {"formulario": formulario, "errores":formulario.errors})
    else:
        formulario = PaisFormulario(initial={"nombre_pais":pais.nombre_pais, "numero_habitantes":pais.num_habitantes})
        return render(request, "app/editar_pais.html", {"formulario":formulario, "errores": ""})

def eliminar_pais(request, id):
    pais = Pais.objects.get(id=id)
    pais.delete()

    return redirect(creacion_pais)

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
    
    continentes = Continente.objects.all().order_by('nombre_continente')
    
    contexto2 = {"continentes":continentes}
    contexto = {"formulario":formulario}

    nuevo_contexto = {**contexto, **contexto2}
    return render(request, 'app/agregar_continente.html', nuevo_contexto)

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
    
    idiomas = Idioma.objects.all().order_by('nombre_idioma')

    contexto2 = {"idiomas":idiomas} 
    contexto = {"formulario":formulario}
    
    nuevo_contexto = {**contexto, **contexto2}
    return render(request, 'app/agregar_idioma.html', nuevo_contexto)