from django.contrib import admin

# Register your models here.
from .models import Categoria, Cliente, Comercio, Usuario, Repartidor,Producto,Pedido,Carrito

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Comercio)
admin.site.register(Usuario)
admin.site.register(Repartidor)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Carrito)