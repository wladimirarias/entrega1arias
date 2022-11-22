from django.urls import path
from app.views import *

urlpatterns = [
    path("inicio/", inicio,  name="app-inicio"),
    path("paises/", paises, name="app-paises"),
    path("paises/crear/", creacion_pais, name="app-paises-crear"),
    path("paises/buscar/", buscar_pais, name="app-paises-buscar"),
    path("paises/actualizar/<id>/", edit_pais, name="app-paises-editar"),
    path("paises/borrar/<id>/", eliminar_pais, name="app-paises-borrar"),
    path("paises/buscar/resultados", resultados_busqueda_paises, name="app-paises-buscar-resultados"),
    path("continentes/", continentes, name="app-continentes"),
    path("continentes/actualizar/<id>/", edit_continente, name="app-continentes-editar"),
    path("continentes/borrar/<id>/", eliminar_continente, name="app-continentes-borrar"),
    path("continentes/crear/", creacion_continente, name="app-continentes-crear"),
    path("idiomas/", idiomas, name="app-idiomas"),
    path("idiomas/actualizar/<id>/", edit_idioma, name="app-idiomas-editar"),
    path("idiomas/borrar/<id>", eliminar_idioma, name="app-idiomas-borrar"),
    path("idiomas/crear/", creacion_idioma, name="app-idiomas-crear"),

    #Definición rutas VBC

    path("paisesvbc/", PaisesList.as_view(), name="app-paisesvbc"),
    path("paisesvbc/detalle/<pk>/", PaisesDetail.as_view(), name="app-paisesvbc-detail"),
    path("paisesvbc/crear/", PaisesCreate.as_view(), name="app-paisesvbc-create"),
    path("paisesvbc/actualizar/<pk>/", PaisesUpdate.as_view(), name="app-paisesvbc-update"),
    path("paisesvbc/borrar/<pk>/", PaisesDelete.as_view(), name="app-paisesvbc-delete"),

    #Rutas para Login
    path("login/", iniciar_sesion, name="auth-login")
]