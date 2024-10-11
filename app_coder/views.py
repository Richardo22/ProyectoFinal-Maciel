from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def crea_producto(req, nombre, ingredientes, precio):
    nuevo_producto = Empanada(nombre=nombre, ingredientes=ingredientes, precio=precio)
    nuevo_producto.save()
    return HttpResponse(f"""
          <p>Producto: {nuevo_producto.nombre} - {nuevo_producto.ingredientes} - {nuevo_producto.precio} creado con exito </p>
""")
def lista_productos(req):
    lista=Empanada.objects.all()
    return render(req, 'lista_empanadas.html', {'empanadas': lista})
def crea_producto(req, nombre, ingredientes, precio):
    nueva_hamburguesa = Hamburguesa(nombre=nombre, ingredientes=ingredientes, precio=precio)
    nueva_hamburguesa.save()
    return HttpResponse(f"""
          <p>Producto: {nueva_hamburguesa.nombre} - {nueva_hamburguesa.ingredientes} - {nueva_hamburguesa.precio} creado con exito </p>
""")
def lista_hamburguesa(req):
    lista=hamburguesa.objects.all()
    return render(req, 'lista_hamburguesa.html', {'hamburguesa': lista})
def crea_producto(req, nombre, ingredientes, precio):
    nueva_pizza = Pizza(nombre=nombre, ingredientes=ingredientes, precio=precio)
    nueva_pizza.save()
    return HttpResponse(f"""
          <p>Producto: {nueva_pizza.nombre} - {nueva_pizza.ingredientes} - {nueva_pizza.precio} creado con exito </p>
""")

def inicio(req):
    return render(req, 'inicio.html', {})
def empanada(req):
    return render(req, 'empanada.html', {})
def hamburguesa(req):
    return render(req, 'hamburguesa.html', {})
def pizza(req):
    return render(req, 'pizza.html', {})
def busqueda_empanada(req):

  return render(req, "busqueda-producto.html")

def buscar_empanada(req):

  nombre = req.GET.get("nombre", "")  
  empanadas = Empanada.objects.filter(nombre__icontains=nombre)
  
  return render(req, "resultado_busqueda.html", {"nombre": nombre, "empanadas": empanadas})
def crea_empanada(req):
    print('method',req.method)
    print('data', req.POST)
    if req.method == 'POST':
        info = req.POST
        mi_formulario=EmpanadaFormulario(
            {
                "nombre":info["nombre"],
                "ingredientes":info["ingredientes"],
                "precio":info["precio"]
            }
        )
        nueva_empanada=Empanada(nombre=info["nombre"],ingredientes=info["ingredientes"],precio=info["precio"])
        nueva_empanada.save()
        return HttpResponse('/inicio.html')
    else:
        return render(req, "empanada_formulario.html",{"mi_formulario": mi_formulario},)
def crear_hamrburguesa(req):
    print('method',req.method)
    print('data', req.POST)
    if req.method == 'POST':
        info = req.POST
        mi_formulario=HamburguesaFormulario(
            {
                "nombre":info["nombre"],
                "ingredientes":info["ingredientes"],
                "precio":info["precio"]
            }
        )
        nueva_hamburguesa=Hamburguesa(nombre=info["nombre"],ingredientes=info["ingredientes"],precio=info["precio"])
        nueva_hamburguesa.save()
        return HttpResponse('/inicio.html')
    else:
        return render(req, "hamburguesa_formulario.html",{"mi_formulario": mi_formulario},)

def empanada_formulario(req):
    print('method', req.method)
    print('data', req.POST)
    if req.method == 'POST':
        mi_formulario=EmpanadaFormulario(req.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            empanada = Empanada(nombre=data['nombre'], ingredientes=data['ingredientes'], precio=data['precio'])
            empanada.save()
            return HttpResponse('inicio.html')
        else:
            return render(req,"empanada_formulario.html",{"mi_formulario": mi_formulario})
    else:
        mi_formulario=EmpanadaFormulario()
        return render(req,"empanada_formulario.html",{"mi_formulario": mi_formulario})
def hamburguesa_formulario(req):
    print('method', req.method)
    print('data', req.POST)
    if req.method == 'POST':
        mi_formulario=HamburguesaFormulario(req.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            hamburguesa = Hamburguesa(nombre=data['nombre'], ingredientes=data['ingredientes'], precio=data['precio'])
            hamburguesa.save()
            return HttpResponse('inicio.html')
        else:
            return render(req,"hamburguesa_formulario.html",{"mi_formulario": mi_formulario})
    else:
        mi_formulario=EmpanadaFormulario()
        return render(req,"hamburguesa_formulario.html",{"mi_formulario": mi_formulario})
def pizza_formulario(req):
    print('method', req.method)
    print('data', req.POST)
    if req.method == 'POST':
        mi_formulario=PizzaFormulario(req.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            pizza = Pizza(nombre=data['nombre'], ingredientes=data['ingredientes'], precio=data['precio'])
            pizza.save()
            return HttpResponse('inicio.html')
        else:
            return render(req,"pizza_formulario.html",{"mi_formulario": mi_formulario})
    else:
        mi_formulario=PizzaFormulario()
        return render(req,"pizza_formulario.html",{"mi_formulario": mi_formulario})    
      
    
def lista_empanadas(req):
    empanadas = Empanada.objects.all()
    return render(req, "lista_empanada.html", {"empanadas": empanadas})
def lista_hamburguesas(req):
    hamburguesas = Hamburguesa.objects.all()
    return render(req, "lista_hamburguesa.html", {"hamburguesas": hamburguesas})
def lista_pizzas(req):
    pizzas = Pizza.objects.all()
    return render(req, "lista_pizza.html", {"pizzas": pizzas})

def eliminar_empanadas(req, id):
    if req.method == 'POST':
        empanada = Empanada.objects.get(id=id)
        empanada.delete()
        empanadas = Empanada.objects.all()
        return render(req, "lista_empanada.html", {"empanadas": empanadas})
def eliminar_hamburguesa(req, id):
    if req.method == 'POST':
        hamburguesa = Hamburguesa.objects.get(id=id)
        hamburguesa.delete()
        hamburguesas = Hamburguesa.objects.all()
        return render(req, "lista_hamburguesa.html", {"hamburguesas": hamburguesas})
def eliminar_pizza(req, id):
    if req.method == 'POST':
        pizza = Hamburguesa.objects.get(id=id)
        pizza.delete()
        pizzas = Hamburguesa.objects.all()
        return render(req, "lista_pizza.html", {"pizzas": pizzas})    
def editar_empanadas(req, id):
    empanada = Empanada.objects.get(id=id)
    if req.method == 'POST':
        mi_formulario = EmpanadaFormulario(req.POST)
        print (mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            empanada.nombre = data['nombre']
            empanada.ingredientes = data['ingredientes']
            empanada.precio = data['precio']
            empanada.save()
            return HttpResponseRedirect('/app_coder/')
        else:
            return render(req, "empanada_formulario.html", {'mi_formulario': mi_formulario})
    else:
        mi_formulario = EmpanadaFormulario(initial={
            'nombre': empanada.nombre,
            'ingredientes': empanada.ingredientes,
            'precio': empanada.precio
        })
    return render(req, 'editar_empanada.html', {'mi_formulario': mi_formulario, "id": empanada.id})
def editar_hamburguesa(req, id):
    hamburguesa = Hamburguesa.objects.get(id=id)
    if req.method == 'POST':
        mi_formulario = HamburguesaFormulario(req.POST)
        print (mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            hamburguesa.nombre = data['nombre']
            hamburguesa.ingredientes = data['ingredientes']
            hamburguesa.precio = data['precio']
            hamburguesa.save()
            return HttpResponseRedirect('/app_coder/')
        else:
            return render(req, "empanada_formulario.html", {'mi_formulario': mi_formulario})
    else:
        mi_formulario = HamburguesaFormulario(initial={
            'nombre': hamburguesa.nombre,
            'ingredientes': hamburguesa.ingredientes,
            'precio': hamburguesa.precio
        })
    return render(req, 'editar_hamburguesa.html', {'mi_formulario': mi_formulario, "id": hamburguesa.id})

def editar_pizza(req, id):
    pizza = Pizza.objects.get(id=id)
    if req.method == 'POST':
        mi_formulario = PizzaFormulario(req.POST)
        print (mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            pizza.nombre = data['nombre']
            pizza.ingredientes = data['ingredientes']
            pizza.precio = data['precio']
            pizza.save()
            return HttpResponseRedirect('/app_coder/')
        else:
            return render(req, "pizza_formulario.html", {'mi_formulario': mi_formulario})
    else:
        mi_formulario = PizzaFormulario(initial={
            'nombre': pizza.nombre,
            'ingredientes': pizza.ingredientes,
            'precio': pizza.precio
        })
    return render(req, 'editar_pizza.html', {'mi_formulario': mi_formulario, "id": pizza.id})







    