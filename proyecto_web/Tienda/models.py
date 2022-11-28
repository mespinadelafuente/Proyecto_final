from django.db import models

# Create your models here.


class CategoriaProducto(models.Model):
    nombre=models.CharField (max_length= 30)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaproducto"
        verbose_name_plural="categoriasproducto"

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField (max_length=50)
    categorias=models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='Tienda', null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"

    def __str__(self) -> str:
        return self.nombre
