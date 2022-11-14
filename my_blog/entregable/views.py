from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def entregables (request) :
    plantilla = loader.get_template ('templates/cursos.html')

    return HttpResponse (plantilla)
