from django.shortcuts import render
from django.http import HttpResponse

def busqueda_productos(request):

    return render (request,"busqueda_productos.html")

def buscar (request):
    mensaje = "Articulo Buscado: %r" %request.GET["producto"]
    return HttpResponse (mensaje)

# Create your views here.
