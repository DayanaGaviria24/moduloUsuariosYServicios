"""usuarioss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios1.views import usuario, crearUsuario, formularioUsuario, editarU, actualizarU
from servicios.views import servicio, crearServicio, formularioServicio, editarS, actualizarS,eliminarS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',usuario),
    path('crearUsuario/',crearUsuario),
    path('formularioUsuario/',formularioUsuario),
    path('editarU/<int:id>',editarU, name='editarUsuario'),
    path('actualizarU/<int:id>',actualizarU, name='actualizarUsuario'),
    
    path('servicio/',servicio),
    path('crearServicio/',crearServicio),
    path('formularioServicio/',formularioServicio),
    path('editarS/<int:id>',editarS, name='editarServicio'),
    path('actualizarS/<int:id>',actualizarS, name='actualizarServicio'),
    path('eliminarS/<int:id>',eliminarS, name='eliminarServicio'),

]
