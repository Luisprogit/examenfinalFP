#---------------- VALIDACIONES DE NÚMEROS ----------------
def leer_entero(mensaje):
    while True:      
        try:
            numero_entero = int(input(mensaje))
            if numero_entero >= 1:
                return numero_entero
        except ValueError:
            print("Debe ingresar un número entero")


def leer_decimal(mensaje):
    while True:
        try:
            numero_decimal = float(input(mensaje))
            if numero_decimal >= 0.01:
                return numero_decimal
        except ValueError:
            print("Debe ingresar un número válido")