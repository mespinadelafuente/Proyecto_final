from django.shortcuts import render
from .models import Producto,CategoriaProducto

# Create your views here.

def Tienda  (request) :
    productos=Producto.objects.all
    return render (request, "Tienda/tienda.html",{'productos':productos})

