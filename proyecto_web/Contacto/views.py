from django.shortcuts import render
from .forms import Formulariocontacto
from django.shortcuts import redirect

# Create your views here.

def contacto (request) :
    formulario_contacto=Formulariocontacto()
    
    if request.method == "POST":
        formulario_contacto=Formulariocontacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?valido")


    return render (request, "Contacto/contacto.html", {"miformulario":formulario_contacto})