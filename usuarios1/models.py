from tkinter import Widget
from django.db import models


# Create your models here.

class Usuarios(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    documento=models.CharField(max_length=10)
    nPersona= models.CharField(max_length=40)
    nUsuario= models.CharField(max_length=20)
    contrasena= models.CharField(max_length=20)
    correo= models.EmailField(blank=False,null=False)
    fechaCreacion= models.DateTimeField(auto_now=True) 