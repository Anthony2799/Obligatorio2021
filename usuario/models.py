from django.db import models


class Entidad(models.Model):
    numero_entidad = models.AutoField(primary_key=True)
    numero_grupo = models.IntegerField(blank=False)
    direccion =  models.CharField(max_length=200,blank=False)
    email = models.EmailField(blank=False)
    telefono = models.CharField(max_length=20,blank=True)



class Perfil_cliente(models.Model):
    entidad_usuario =  models.ForeignKey('usuario.Entidad', verbose_name='numero_entidad', on_delete=models.CASCADE)
    nombre_usuario = models.TextField(max_length=40,blank=False)
    apellido_usuario = models.TextField(max_length=40,blank=False)
    documento_usuario = models.TextField(max_length=20,primary_key=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modficado = models.DateTimeField(auto_now=True) 
    
    


class Perfil_empresa(models.Model):
    entidad_usuario = models.ForeignKey('usuario.Entidad', verbose_name='numero_entidad', on_delete=models.CASCADE)
    rut = models.TextField(max_length=12,primary_key=True)
    razon_social = models.TextField(max_length=50,blank=False)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modficado = models.DateTimeField(auto_now=True) 



class Perfil_funcionario(models.Model):

    documento_funcionario = models.TextField(max_length=20,primary_key=True)
    nombre_funcionario = models.TextField(max_length=40,blank=False)
    apellido_funcionario = models.TextField(max_length=40,blank=False)
    Contraseña  = models.CharField(max_length= 20, blank= False, null= False)

