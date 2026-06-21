#---------------- CLASE VENTA ----------------
class Venta:
    def __init__(self, cliente, producto, cantidad, precio, pagado):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.pagado = pagado
        self.total = cantidad * precio