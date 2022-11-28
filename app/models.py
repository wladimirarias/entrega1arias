from django.db import models
from django.contrib.auth.models import User

# Creación de Modelos

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=50)
    num_habitantes = models.IntegerField()

class Continente(models.Model):
    nombre_continente = models.CharField(max_length=50)
    nivel_economia = models.CharField(max_length=50)

class Idioma(models.Model):
    nombre_idioma = models.CharField(max_length=50)
    origen_idioma = models.CharField(max_length=50)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)