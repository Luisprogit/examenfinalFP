#---------------- VALIDACIONES DE NÚMEROS ----------------
def leer_entero(mensaje):
    while True:      
        try:
            numero_entero = int(input(mensaje))
            if numero_entero >= 1:
                return numero_entero
            
            print("Ingresa nuevamente. Solo valores mayor o igual a 1")
        except ValueError:
            print("Ingresa nuevamente. Solo se permite números enteros")

#---------------- VALIDACIÓN DE NOMBRE ----------------

def validar_nombre(mensaje):
    while True:
        valor = input(mensaje).strip().capitalize()
        if valor.replace(" ", "").isalpha() and len(valor) > 0:
            return valor
        print("Ingrese nuevamente. El nombre debe tener solo letras y no estar vacío")

#---------------- VALIDACIÓN DE OPCIÓN DE PAGAR ----------------

def validar_opcion(mensaje):
    while True:
        valor = input(mensaje).strip().lower()
        if valor == 's' or valor == 'n':
            return valor
        print("Ingrese nuevamente. Debe colocar s para Si o n para No")

#---------------- VALIDACIÓN DE OPCIÓN DE ELECCIÓN DE MENU ----------------

def validar_opcion_lista(mensaje, total_opciones):
    while True:
        valor = input(mensaje).strip()

        if valor.isdigit():
            opcion = int(valor)

            if 1 <= opcion <= total_opciones:
                return opcion 
                
        print(f"Ingrese nuevamente. Solo opciones del 1 al {total_opciones}")

