from django.urls import path, reverse_lazy
from .views import Vregistro,cerrar_sesion,logear

urlpatterns = [

    path ('', Vregistro.as_view(), name='Autenticacion') ,

    path ('cerrar_sesion', cerrar_sesion, name='cerrar_sesion') ,

    path ('logear', logear, name='logear') ,


]