from django import forms

class Formulariocontacto (forms.Form):
    nombre=forms.CharField (label="Nombre", required=True)
    email=forms.CharField (label="Email", required=True)

    contenido=forms.CharField (widget=forms.Textarea,label="Contenido", required=True)
