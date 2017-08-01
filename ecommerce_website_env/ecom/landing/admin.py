# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import Proveedor
from .models import Cliente
from .models import Pedido
from .models import Carrito


class proveedor_admin(admin.ModelAdmin):
    list_display = ["__str__", "compania"]
    class Meta:
        model = Proveedor


#clase que permite mostrar mas detalles en la pantalla de admin
class producto_admin(admin.ModelAdmin):
    list_display = ["__str__", "description", "precio"]
    class Meta:
        model = Producto


class cliente_admin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Cliente



class pedido_admin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Pedido

class carrito_admin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Carrito


admin.site.register(Producto, producto_admin)
admin.site.register(Proveedor, proveedor_admin)
admin.site.register(Cliente, cliente_admin)
admin.site.register(Pedido, pedido_admin)
admin.site.register(Carrito, carrito_admin)
