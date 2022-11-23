from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Pais, Continente, Idioma
from app.forms import PaisFormulario, ContinenteFormulario, IdiomaFormulario, UserRegisterForm
from django.core.paginator import Paginator
from django.http import Http404

#Import vistas basadas en Clases
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Imports de Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#Protección para sesiones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Creación vistas

#@login_required
def inicio (request):
    return render(request, 'app/index.html')

@login_required
def paises (request):
    return render(request, 'app/agregar_pais.html')

@login_required
def buscar_pais(request):
    
    return render(request, 'app/busqueda_paises.html')

@login_required
def resultados_busqueda_paises(request):
    nombre_pais = request.GET['nombre_pais']

    paises = Pais.objects.filter(nombre_pais__icontains=nombre_pais)
    return render(request, 'app/resultados_busquedas_paises.html', {"paises": paises})

@login_required
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

@login_required
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

@login_required
def eliminar_pais(request, id):
    pais = Pais.objects.get(id=id)
    pais.delete()

    return redirect(creacion_pais)

@login_required
def continentes (request):
    return render(request, 'app/agregar_continente.html')

@login_required
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
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(continentes, 5)
        continentes = paginator.page(page)
    except:
        raise Http404
    
    #contexto2 = {"continentes":continentes} Cambio por agregación de paginador
    contexto2 = {"entity":continentes, "paginator":paginator}
    contexto = {"formulario":formulario}

    nuevo_contexto = {**contexto, **contexto2}
    return render(request, 'app/agregar_continente.html', nuevo_contexto)

@login_required
def edit_continente(request, id):
    continente = Continente.objects.get(id=id)

    if request.method == 'POST':
        formulario = ContinenteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            continente.nombre_continente = data["nombre_continente"]
            continente.nivel_economia = data["nivel_economia"]
            continente.save()
            return redirect(creacion_continente)
        else:
            return render(request, "app/editar_continente.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = ContinenteFormulario(initial={"nombre_continente":continente.nombre_continente, "nivel_economia":continente.nivel_economia})
        return render(request, "app/editar_continente.html", {"formulario":formulario, "errores":""})

@login_required
def eliminar_continente(request, id):
    continente = Continente.objects.get(id=id)
    continente.delete()

    return redirect(creacion_continente)

@login_required
def idiomas (request):
    return render(request, 'app/agregar_idioma.html')

@login_required
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
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(idiomas, 5)
        idiomas = paginator.page(page)
    except:
        raise Http404

    #contexto2 = {"idiomas":idiomas} 
    contexto2 = {"entity":idiomas, "paginator":paginator} 
    contexto = {"formulario":formulario}
    
    nuevo_contexto = {**contexto, **contexto2}
    return render(request, 'app/agregar_idioma.html', nuevo_contexto)

@login_required
def edit_idioma(request, id):
    idioma = Idioma.objects.get(id=id)

    if request.method == 'POST':
        formulario = IdiomaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            idioma.nombre_idioma = data["nombre_idioma"]
            idioma.origen_idioma = data["origen_idioma"]
            idioma.save()
            return redirect(creacion_idioma)
        else:
            return render(request, "app/editar_idioma.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = IdiomaFormulario(initial={"nombre_idioma":idioma.nombre_idioma, "origen_idioma":idioma.origen_idioma})
        return render(request, "app/editar_idioma.html", {"formulario":formulario, "errores": ""})

@login_required
def eliminar_idioma(request, id):
    idioma = Idioma.objects.get(id=id)
    idioma.delete()

    return redirect(creacion_idioma)

#Creación vistas basadas en clases

class PaisesList(LoginRequiredMixin, ListView):
    model = Pais
    template_name = "app/paises_list.html"
    paginate_by = 4

class PaisesDetail(LoginRequiredMixin, DetailView):
    model = Pais
    template_name = "app/paises_detail.html"

class PaisesCreate(LoginRequiredMixin, CreateView):
    model = Pais
    success_url = "/paisesvbc/"
    fields = ["nombre_pais", "num_habitantes"]
    template_name = "app/paises_form.html"

class PaisesUpdate(LoginRequiredMixin, UpdateView):
    model = Pais
    success_url = "/paisesvbc/"
    fields = ["nombre_pais", "num_habitantes"]
    template_name = "app/paises_form.html"

class PaisesDelete(LoginRequiredMixin, DeleteView):
    model = Pais
    success_url = "/paisesvbc/"
    template_name = "app/paises_confirm_delete.html"

#Funciones para Login

def iniciar_sesion(request):
    errors = ""

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("app-inicio")
            else:
                return render(request, "app/login.html", {"form": formulario, "errors": "Credenciales Inválidas"})
        else:
            return render(request, "app/login.html", {"form": formulario, "errors": errors})

    formulario = AuthenticationForm()
    return render(request, "app/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("app-inicio")
        else:
            return render(request, "app/register.html", {"form": formulario , "errors": formulario.errors})
    
    formulario = UserRegisterForm()
    return render(request, "app/register.html", {"form": formulario})