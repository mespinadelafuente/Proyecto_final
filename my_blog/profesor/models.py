from django.db import models

# Create your models here.
class profesor (models.Model) : 
    nombre = models.CharField (max_length=30)
    apellido = models.CharField (max_length=30)
    email = models.EmailField ()
    profesion = models.CharField (max_length=30)
    