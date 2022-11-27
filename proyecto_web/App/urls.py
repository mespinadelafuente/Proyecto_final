from django.urls import path
from App import views

urlpatterns = [
    path ('', views.home, name='Home'),
    path ('about/', views.about, name='About'),
    path ('tienda/', views.tienda, name='Tienda'),
    path ('blog/', views.blog, name='Blog'),
    path ('contacto/', views.contacto, name='Contacto'),
    path ('servicios/', views.servicios, name='Servicios') ,
]

