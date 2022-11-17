from django.urls import path
from app.views import *

urlpatterns = [
    path("", inicio,  name="app-inicio"),
    path("paises/", paises, name="app-paises"),
    path("paises/crear/", creacion_pais, name="app-paises-crear"),
    path("paises/buscar/", buscar_pais, name="app-paises-buscar"),
    path("paises/actualizar/<id>/", edit_pais, name="app-paises-editar"),
    path("paises/borrar/<id>/", eliminar_pais, name="app-paises-borrar"),
    path("paises/buscar/resultados", resultados_busqueda_paises, name="app-paises-buscar-resultados"),
    path("contienentes/", continentes, name="app-continentes"),
    path("continentes/crear/", creacion_continente, name="app-continentes-crear"),
    path("idiomas/", idiomas, name="app-idiomas"),
    path("idiomas/crear/", creacion_idioma, name="app-idiomas-crear")
]