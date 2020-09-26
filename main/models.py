from django.db import models

# Create your models here.
class Comercio(models.Model):
    rucComercio = models.CharField(max_length=11)
    nombreComercio = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rucComercio} | {self.nombreComercio}'

class Categoria(models.Model):
    idCategoria = models.CharField(max_length=10)
    nombreCategoria = models.CharField(max_length=20)
    listaProductos = models.TextField()

    def __str__(self):
        return f'{self.idCategoria} | {self.nombreCategoria}'

class Usuario(models.Model):
    dni = models.CharField(max_length=8)
    nombreUsuario = models.CharField(max_length=20)
    apPaterno = models.CharField(max_length=20)
    apMaterno = models.CharField(max_length=20)
    correoUsuario = models.CharField(max_length=20)
    telefonoUsuario = models.CharField(max_length=20)
    tarjetaBancaria = models.CharField(max_length=20)
    usuarioAcceso = models.CharField(max_length=20)
    contraseñaAcceso = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.dni} | {self.nombreUsuario}'

class Cliente(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

    idCliente = models.CharField(max_length=10)
    listaProductosTop = models.TextField()
    frecuenciaCompra = models.CharField(max_length=20)
    listaPedidos = models.TextField()
    
    def __str__(self):
        return f'{self.idCliente}'

class Repartidor(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)

    codigoRepartidor =models.CharField(max_length=20)
    nombreRepartidor = models.CharField(max_length=20)
    apPaternoRepartidor = models.CharField(max_length=20)
    apMaternoRepartidor = models.CharField(max_length=20)
    correoRepartidor = models.CharField(max_length=20)
    telefonoRepartidor = models.CharField(max_length=20)
    listaPedidos = models.TextField()

    def __str__(self):
        return f'{self.codigoRepartidor} | {self.nombreRepartidor}'

class Producto(models.Model):
    comercio = models.ForeignKey('Comercio', on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

    idProducto = models.CharField(max_length=10)
    nombreProducto = models.CharField(max_length=20)
    descripcion = models.TextField
    precio = models.FloatField()

    def __str__(self):
        return f'{self.idProducto} | {self.nombreProducto}'

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    repartidor = models.ForeignKey('Repartidor', on_delete=models.SET_NULL, null=True)

    nroPedido = models.CharField(max_length=10)
    fechaCreacion = models.DateField()
    fechaEntrega = models.DateField()
    costoEnvio = models.FloatField()
    direccionEntrega = models.CharField(max_length=30)
    direccionOrigen = models.CharField(max_length=30)
    estadoPedido = models.CharField(max_length=20)
    precioTotal = models.FloatField()

    def __str__(self):
        return {self.nroPedido} 

class Carrito(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)

    precioUnitario = models.FloatField()
    cantidad = models.IntegerField(default=1)
    precioSubtotal = models.FloatField()

    def __str__(self):
        return {self.precioSubtotal} 

    
    #def precio_subtotal(self):
        #return self.precioUnitario * self.cantidad
