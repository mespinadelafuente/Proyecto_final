from django.shortcuts import render
from django.http import  HttpResponse
from Carro.carro import Carro
# Create your views here.

def home (request) :

    carro=Carro(request)
    return render (request, "App/home.html")

def about (request) :
    return render (request, "App/about.html")






