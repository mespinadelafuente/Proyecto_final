from django.shortcuts import render
from django.http import HttpResponse
from curso.models import Curso
from django.template import loader


# Create your views here.

def curso (self) : 
    curso = Curso (nombre = "Desarrollo web", clase = "19881")
    curso.save ()
    documentosdetexto = f" Curso : {curso.nombre} Clase: {curso.clase} "

    return HttpResponse (documentosdetexto)



def cursos (request) :
    loader.get_template ('cursos.html') 
    return render (request, "cursos.html")
