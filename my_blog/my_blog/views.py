from django.http import HttpResponse
from django.template import Context, Template


def saludo (request):
    return HttpResponse ("Hola django-coder")

def probandotemplate (self):
    miHtml = open ("C:/Users/Martin D/documents/proyectos_coder/proyecto_final/my_blog/templates/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close() 

    miContexto= Context ()
    documento = plantilla.render(miContexto)

    return HttpResponse (documento)