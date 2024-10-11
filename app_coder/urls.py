from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('agregar-producto/<nombre>/<ingredientes>/<precio>', crea_producto),
    path('lista_empanadas/', lista_productos),   
    path('',inicio,name='Inicio'),  
    path('empanada/',empanada, name='empanada'),
    path('pizza/',pizza, name='pizza'),
    path('hamburguesa/',hamburguesa, name='hamburguesa'),
    path('empanada-formulario/',empanada_formulario, name='EmpanadaFormulario'),
    path('hamburguesa-formulario/',hamburguesa_formulario, name='HamburguesaFormulario'),
    path('pizza-formulario/',pizza_formulario, name='PizzaFormulario'),
    # path('busqueda-producto/',busqueda_empanada, name='BusquedaProducto'),
    path('buscar-empanada/',buscar_empanada, name='BuscarEmpanada'),
    path('lista_empanada/',lista_empanadas, name='ListaEmpanada'),
    path('lista_hamburguesa/',lista_hamburguesas, name='ListaHamburguesa'),
    path('lista_pizza/',lista_pizzas, name='ListaPizza'),

    ]