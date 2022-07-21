from django.shortcuts import HttpResponse, render

def home(request):
    return render(request,"EstuProfeApp/home.html")

def inicio(request):
    return render(request,"EstuProfeApp/inicio.html")
    
def perfil(request):
   return render(request,"EstuProfeApp/perfil.html")

def publicaciones(request):
    return render(request,"EstuProfeApp/publicaciones.html")
def crearCuenta(request):
    return render(request,"EstuProfeApp/createAcount.html")

