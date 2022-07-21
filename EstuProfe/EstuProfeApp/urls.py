from django.urls import path
from EstuProfeApp import views


urlpatterns = [
    path('',views.home, name = "Home"),
    path('inicio',views.inicio, name = "Inicio"),
    path('perfil',views.perfil, name = "Perfil"),
    path('publicaciones',views.publicaciones, name = "Publicaciones"),
    path('crearCuenta',views.crearCuenta, name = "CrearCuenta"),
]