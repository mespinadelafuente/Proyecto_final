from django.contrib import admin
from .models import CategoriaProducto, Producto
# Register your models here.

class Categoriaproductoadmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')

class Productoadmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(CategoriaProducto,Categoriaproductoadmin)
admin.site.register(Producto,Productoadmin)

