from django.contrib import admin
from gestiondepedidos.models import Clientes,Articulos,Pedidos
# Register your models here.

class Clientesadmin (admin.ModelAdmin):
    list_display = ("nombre", "apellido" , "telefono")
    search_fields = ("nombre", "apellido", "telefono")

class Articulosadmin (admin.ModelAdmin):
    list_display = ("nombre","categoria", "precio")
    list_filter = ("nombre", "categoria",)

class Pedidosadmin (admin.ModelAdmin) :
    list_filter = ("fecha",)
    date_hierarchy = "fecha"
    
admin.site.register(Clientes, Clientesadmin)
admin.site.register(Articulos,Articulosadmin)
admin.site.register(Pedidos,Pedidosadmin)

