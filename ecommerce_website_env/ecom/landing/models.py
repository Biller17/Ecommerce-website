# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Proveedor(models.Model):
    #relacion con modelo de usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    compania = models.CharField(max_length = 20, blank = False, null = False)
    #nombre = models.CharField(max_length = 20, blank = False, null = False)
    #apellido = models.CharField(max_length = 20, blank = False, null = False )
    direccion = models.CharField(max_length = 50, blank = False, null = False)
    delegacion = models.CharField(max_length = 20, blank = False, null = False)
    estado = models.CharField(max_length = 20, blank = False, null = False)
    codigo_postal = models.CharField(max_length = 10, blank = False, null = False)
    telefono = models.CharField(max_length = 20, blank = False, null = False)
    #correo = models.CharField(max_length = 20, blank = False, null = False)
    pagina = models.CharField(max_length = 30, default = "Sin página disponible")
    logo = models.ImageField(upload_to = 'logos_proveedores', null = True, blank = True)
    #password = models.CharField(max_length = 20, blank = False, null = False)

    def __str__(self):
        return self.compania



class Producto(models.Model):
    nombre = models.CharField(max_length=20, default="Product Name") #titulo del producto
    description = models.TextField() #descrip del producto
    sku = models.CharField(max_length = 30, default = "0000000")
    cantidad_por_unidad = models.IntegerField(default = 1)
    precio = models.DecimalField(max_digits = 50, decimal_places = 2, default = 0.00)
    color = models.CharField(max_length = 20, default="No color") #color del producto
    PEQUENO = 'P'
    MEDIANO = 'M'
    GRANDE =  'G'
    TAMANO_CHOICES = (
        (PEQUENO, 'Pequeño'),
        (MEDIANO, 'Mediano'),
        (GRANDE, 'Grande'),
    )
    tamano = models.CharField(
        max_length = 1,
        choices = TAMANO_CHOICES,
        default = MEDIANO,
    )
    descuento = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    peso_unidad = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    stock = models.IntegerField(default = 0)
    producto_disponible = models.BooleanField(default = False)
    imagen = models.ImageField(upload_to = 'imagenes_productos', null = True, blank = True)
    proveedor = models.ForeignKey(Proveedor , on_delete = models.CASCADE, null = True, blank = True)


    def __str__(self):
        return self.nombre



class Cliente(models.Model):
        #relacion con modelo de usuario
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        direccion = models.CharField(max_length = 50, blank = False, null = False)
        delegacion = models.CharField(max_length = 20, blank = False, null = False)
        estado = models.CharField(max_length = 20, blank = False, null = False)
        codigo_postal = models.CharField(max_length = 10, blank = False, null = False)
        telefono = models.CharField(max_length = 20, blank = False, null = False)
        direccion_envio = models.CharField(max_length = 50, blank = False, null = False)
        delegacion_envio = models.CharField(max_length = 20, blank = False, null = False)
        estado_envio = models.CharField(max_length = 20, blank = False, null = False)
        codigo_postal_envio = models.CharField(max_length = 15, blank = False, null = False)

        def __str__(self):
            return self.user


class Pedido(models.Model):
        productos = models.ManyToManyField(Producto)
        #agregar field de pago
        pagado = models.BooleanField(default = False)
        cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
        fecha_pedido = models.DateField(blank = False, null = False)
        fecha_entrega = models.DateField(blank = True, null = True)
        fecha_envio = models.DateField(blank = True, null = True)
        entregado = models.BooleanField(default = False)


        def __str__(self):
            return self

class Carrito(models.Model):
        productos = models.ManyToManyField(Producto)
        cliente = models.OneToOneField(Cliente, on_delete = models.CASCADE)
        total = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)

        def __str__(self):
            return self
