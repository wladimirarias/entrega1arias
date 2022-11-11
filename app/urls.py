from django.urls import path
from app.views import *

urlpatterns = [
    path("", inicio,  name="app-inicio"),
]