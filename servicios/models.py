from django.db import models

# Create your models here.

class Servicios(models.Model):
    idServicio=models.AutoField(primary_key=True)
    nServicio=models.CharField(max_length=50)
    #iServicio= models.CharField(max_length=40)
    tiempo= models.IntegerField()
    precio= models.FloatField(max_length=6)