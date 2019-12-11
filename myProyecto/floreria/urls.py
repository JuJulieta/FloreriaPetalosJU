from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home_admin/',home_admin,name='home_admin'),
    path('home_usu/',home_usu,name='home_usu'),
    path('galeria_admin/',galeria_admin,name='galeria_admin'),
    path('galeria_usu/',galeria_usu,name='galeria_usu'),
    path('formulario/',formulario,name='formulario'),
    path('eliminar_flor/<id>/',eliminar_flor,name='eliminar'),
    path('login_inicio/',login_inicio,name='login_inicio'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('login/',login,name='login'),
    path('carrito/',carrito,name='CARRITO'),
    path('agregar_carro/<id>/',agregar_carro,name='AGREGAR_CARRO'),
    path('carro_mas/<id>/',carro_compras_mas,name='CARRO_MAS'),
    path('carro_menos/<id>/',carro_compras_menos,name='CARRO_MENOS'),
    path('grabar_carro/',grabar_carro,name='GRABAR_CARRO'),
    path('vaciar_carrito/',vaciar_carrito,name='VACIAR'),
    path('',home,name='home'),
    path('registro/',registro,name='registro'),
]