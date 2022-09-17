from django.shortcuts import render, redirect
from django.http import HttpResponse
from servicios.models import Servicios

# Create your views here.

def servicio(request):
    servicio=Servicios.objects.filter()
    context={"servicio":servicio}
    return render(request,"servicios.html",context)


def formularioServicio(request):
    return render(request,'crearServicio.html')


def crearServicio(request):
    nombreServicio= request.POST['nombre']
    #insumosServicio= request.POST['insumos']
    tiempoServicio= request.POST['tiempo']
    precioServicio= request.POST['precio']

    servicios=Servicios(nServicio=nombreServicio,tiempo=tiempoServicio,precio=precioServicio) #Falta insumos.
    servicios.save()
    return redirect("/servicio/")


def editarS(request, id):
    mostrar=Servicios.objects.filter(idServicio=id).first()
    context={"mostrar":mostrar}
    return render(request,"editarServicio.html",context)
    

def actualizarS(request, id):

    nombreServicio= request.GET['nombre']
    #insumosServicio= request.GET[' ']
    tiempoServicio = request.GET['tiempo']
    precioServicio = request.GET['precio']
    
    actualizar=Servicios.objects.get(idServicio=id)
    actualizar.nServicio=nombreServicio #Será este?
    actualizar.tiempo=tiempoServicio 
    actualizar.precio=precioServicio

    actualizar.save()
    return redirect("/servicio/")


def eliminarS(request, id):   
    registro= Servicios.objects.get(idServicio=id)
    registro.delete() 
    return redirect("/servicio/")    


