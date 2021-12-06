from django.db import models


class Envio(models.Model):
    costo = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=20)
    peso_paquete = models.FloatField(blank=False, null=False)
    numero_entidad = models.ForeignKey("usuario.Entidad", verbose_name='numero_entidad', on_delete=models.CASCADE)
    documento_usuario = models.ForeignKey("usuario.Perfil_funcionario", verbose_name='documento_funcionario',
                                          on_delete=models.CASCADE)
    Latitud = models.CharField(max_length=20, blank=True)
    Longitud = models.CharField(max_length=20, blank=True)
    distancia = models.FloatField(blank = True, null= True)

