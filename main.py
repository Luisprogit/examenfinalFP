from jugueria import Jugueria
#---------------- Bloque principal ----------------
## Creamos el objeto menu
menu = Jugueria()

while True:
    print("\n===== JUGUERÍA ACUARIO =====")
    print("1. Registrar venta")
    print("2. Consultar deudores")
    print("3. Ordenar ventas")
    print("4. Ver balance")
    print("5. Modificar de fiado a pagado")
    print("6. Salir")
    print("============================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        
        menu.registrar_venta()

    elif opcion == "2":
        menu.consultar_deudores()

    elif opcion == "3":
        menu.ordenar_ventas()

    elif opcion == "4":
        menu.ver_balance()
    
    elif opcion == "5":
        menu.modificar_deudor()

    elif opcion == "6":
        print("Saliendo del sistema de la Juguería Acuario...")
        break

    else:
        print("Opción incorrecta, intente de nuevo")
        