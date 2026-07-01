# ---------------- GUARDAR VENTAS REALIZADAS EN ARCHIVO .TXT ----------------
def guardar_venta(venta):
    with open("ventas.txt", "a", encoding="utf-8") as f:
        f.write(f"{venta.cliente}|{venta.producto}|{venta.cantidad}|{venta.precio}|{venta.pagado}\n")

