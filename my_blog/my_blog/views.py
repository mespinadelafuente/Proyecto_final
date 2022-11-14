from django.http import HttpResponse
from django.template import Context, Template
from django.template import loader

def saludo (request):
    return HttpResponse ("Hola django-coder")

def probandotemplate (self):
    nom = 'Martin'
    ap = 'David'
    diccionario = {"nombre": nom , "apellido":ap }
   # miHtml = open ("C:/Users/Martin D/documents/proyectos_coder/proyecto_final/my_blog/templates/template1.html")
   # plantilla = Template(miHtml.read())
    #miHtml.close() 
    #miContexto= Context (diccionario)
    #documento = plantilla.render(miContexto)
    plantilla = loader.get_template ('template1.html')
    documento = plantilla.render(diccionario) 
    return HttpResponse (documento)

