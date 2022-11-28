from django.shortcuts import render
from django.http import  HttpResponse
from Servicios.models import Servicio
# Create your views here.

def home (request) :
    return render (request, "App/home.html")

def about (request) :
    return render (request, "App/about.html")

def tienda  (request) :
    return render (request, "App/tienda.html")

def contacto (request) :
    return render (request, "App/contacto.html")


