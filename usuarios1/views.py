from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios1.models import Usuarios

# Create your views here.


def usuario(request):
    usuario=Usuarios.objects.filter()
    context={"usuario":usuario}
    return render(request,"usuarios.html",context)


def formularioUsuario(request):
    return render(request,'crearUsuario.html')


def crearUsuario(request):
    documentoUsuario= request.POST['documento']
    nombrePersona= request.POST['nombre']
    nombreUsuario= request.POST['usuario']
    password= request.POST['contrasena']
    correo= request.POST['correo']
    usuarios=Usuarios(documento=documentoUsuario,nPersona=nombrePersona,nUsuario=nombreUsuario,contrasena=password,correo=correo)
    usuarios.save()
    return redirect("/usuario/")


def editarU(request, id):
    mostrar=Usuarios.objects.filter(idUsuario=id).first()
    context={"mostrar":mostrar}
    return render(request,"editarUsuario.html",context)
    

def actualizarU(request, id):

    nombrePersona= request.GET['nombre']
    nombreUsuario= request.GET['usuario']
    correo = request.GET['correo']
    password = request.GET['contrasena']
    
    actualizar=Usuarios.objects.get(idUsuario=id)
    actualizar.nPersona=nombrePersona #Será este?
    actualizar.nUsuario=nombreUsuario 
    actualizar.correo=correo
    actualizar.contrasena=password
    actualizar.save()
    return redirect("/usuario/")