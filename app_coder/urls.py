from django.urls import path
from django.contrib.auth.views import LogoutView
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
    path('elimina_empanada/<int:id>',eliminar_empanadas, name='EliminarEmpanadas'),
    path('modificar_empanada/<int:id>',editar_empanadas, name='ModificarEmpanadas'),
    path('elimina_hamburgesa/<int:id>',eliminar_hamburguesa, name='EliminarHamburguesa'),
    path('modifica_hamburguesa/<int:id>',editar_hamburguesa, name='ModificaHamburguesa'),
    path('acerca_demi',acerca_demi,name='AcercadeMi'),
    path('elimina_pizza/<int:id>',eliminar_pizza, name='EliminarPizza'),
    path('modifica_pizza/<int:id>',editar_pizza, name='ModificarPizza'),
    path('login/',login_view, name='Login'),
    path('registrar/',register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
    ]