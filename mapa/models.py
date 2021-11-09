from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.




class Zona(models.Model):
    nombre_zona = models.CharField(max_length=50, blank=False)


class Ubicacion_zona(models.Model):
    latitud = models.CharField(max_length=50, blank=False)
    longitud = models.CharField(max_length=50, blank=False)
    nro_zona = models.ForeignKey('mapa.Zona', verbose_name='id', on_delete=CASCADE,blank=False)


class Vehiculo_distribuidora(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nro_zona = models.ForeignKey("mapa.Zona", verbose_name= 'id', on_delete=CASCADE, blank=False)
    estado_vehiculo = models.CharField(max_length=20, blank=False)
    capacidad = models.FloatField(blank=False)