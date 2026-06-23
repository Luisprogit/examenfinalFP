from venta import Venta
from validaciones import leer_entero
from archivo import guardar_venta

class Jugueria:
    #---------------- Método constructor ----------------
    def __init__(self):
        ## SE DEFINEN LOS ATRIBUTOS
        self.ventas = []
        self.jugos = ["Jugo de Papaya", "Jugo de Mango", "Jugo Surtido", 
                      "Jugo de fresa c/leche", "Jugo de plátano c/leche", 
                      "Jugo de mango c/leche", "Jugo de naranja"]
        self.precios_jugos = [6.0, 8.0, 7.0, 9.0, 8.0, 9.0, 3.0]
        self.sandwiches = ["Pan con pollo", "Pan con tortilla", "Pan con aceituna", 
                           "Pan con palta", "Pan con hot dog", "Pan con queso fresco", "Pan con lomo"]
        self.precios_sandwiches = [3.5, 2.5, 2.5, 2.5, 2.5, 2.5, 4.0]
        ## CARGA DATOS DEL HISTORIAL DE VENTAS INGRESADOS 
        self.cargar_ventas()

    # ---------------- Registro de ventas ----------------
    def registrar_venta(self):
        ## CARTA DE SANDWICHES
        print("\n===== SANDWICHES - JUGUERÍA ACUARIO =====")
        for i, s in enumerate(self.sandwiches, 1):
            print(f"{i}. {s} - S/ {self.precios_sandwiches[i-1]:.2f}")
        opc_s = int(input("Seleccione número de sándwich: ")) - 1
        
        ## CARTA DE JUGOS
        print("\n===== JUGOS - JUGUERÍA ACUARIO =====")
        for i, j in enumerate(self.jugos, 1):
            print(f"{i}. {j} - S/ {self.precios_jugos[i-1]:.2f}")
        opc_j = int(input("Seleccione número de jugo: ")) - 1

        ## DATOS EXTRAS PARA INGRESAR AL SISTEMA
        cliente = input("Nombre del cliente: ")
        cantidad = leer_entero("Cantidad de combos: ")
        pagado = input("¿Pagó? (s/n): ").strip().lower()
        
        ## SE CALCULA EL TOTAL Y SE ARMAN LOS COMBOS DE SANDWICHES CON JUGOS
        precio_combo = self.precios_sandwiches[opc_s] + self.precios_jugos[opc_j]
        total = cantidad * precio_combo
        nombre_producto = f"{self.sandwiches[opc_s]} + {self.jugos[opc_j]}"

        ## SE CREA EL OBJETO VENTA Y SE AÑADE CON APPEND LA VENTA REALIZADA A LA LISTA
        venta = Venta(cliente, nombre_producto, cantidad, precio_combo, pagado)
        self.ventas.append(venta)
        
        ## SE LLAMA A LA FUNCION Y SE COLOCA COMO PARAMETRO AL OBJETO VENTA
        guardar_venta(venta)

        print(f"Venta registrada. Total: S/ {total:.2f}")

    # ---------------- Cargar ventas ----------------
    def cargar_ventas(self):
        
        self.ventas = []
        try:
            with open("ventas.txt", "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    cliente, producto, cantidad, precio, pagado = linea.split("|")
                    
                    venta = Venta(cliente, producto, int(cantidad), float(precio), pagado)
                    self.ventas.append(venta)
        except FileNotFoundError:
            print("No existe archivo de ventas. Se iniciará vacío")

    # ---------------- Deudores ----------------
    def consultar_deudores(self):
        ## SE CREA VARIABLE QUE INDICARÁ LA EXISTENCIA DE CLIENTES QUE SE FIAN
        hay_deudores = False
        print("\n=== DEUDORES ===")
        
        for v in self.ventas:
            if v.pagado == "n":
                print(f"{v.cliente}: S/ {v.total:.2f}")
                hay_deudores = True
                
        if not hay_deudores:
            print("No hay deudores.")

    # ---------------- Ordenamiento Burbuja ----------------
    def ordenar_ventas(self):
        ## ORDENA COLOCANDO PRIMERO AL MAYOR TOTAL DEL PEDIDO
        n = len(self.ventas)
        for i in range(n):
            for j in range(n - i - 1):
                if self.ventas[j].total < self.ventas[j + 1].total:
                    self.ventas[j], self.ventas[j + 1] = self.ventas[j + 1], self.ventas[j]

        print("\n=== VENTAS ORDENADAS ===")
        
        for v in self.ventas:
            if v.pagado == "s":
                estado = "Pagado"
            if v.pagado == "n":
                estado = "Fiado"
            print(f"Cliente: {v.cliente} | Producto: {v.producto} |{estado}| Total: S/ {v.total:.2f}")
            
    # ------------ Modificación de Deudor a Pagado ------------
    def modifica_deudor(self):
        buscar = input("Nombre del cliente deudor: ").strip().lower()
        
        for v in self.ventas:
            if v.cliente.lower() == buscar and v.pagado == "n":
                v.pagado = "s"  
                
        ## Modifica en el archivo de texto - Pasa de fiado a pagado
                with open("ventas.txt", "w") as f:
                    for venta in self.ventas:
                        f.write(f"{venta.cliente}|{venta.producto}|{venta.cantidad}|{venta.precio}|{venta.pagado}\n")
                
                print(f"El pedido de {v.cliente} está pagado")
                return
        print("No se encontró ningún deudor con el nombre ingresado")

    # ---------------- Balance ----------------
    def ver_balance(self):
        ## INICIALIZAMOS LAS VARIABLES
        ingresos = 0
        deben = 0
        
        for v in self.ventas:
            if v.pagado == "s":
                ingresos += v.total
            elif v.pagado == "n":
                deben += v.total
                
        print("\n=== BALANCE ===")
        print(f"Ingresos: S/ {ingresos:.2f}")
        print(f"Deben: S/ {deben:.2f}")
