import tkinter as tk
from tkinter import messagebox
import random


def crear_inventario():
    flores = ["tulipán", "lirio", "rosa", "dahlia", "margarita", "girasol", "clavel", "geranio"]
    seleccion = random.sample(flores, 3)
    return {
        flor: {
            "precio": random.randint(2000, 6000),
            "cantidad": random.randint(10, 50),
            "vendidas": 0
        } for flor in seleccion
    }

inventario = crear_inventario()
total_ganado = 0


def vender():
    global total_ganado
    flor = flor_var.get()
    try:
        cantidad = int(cantidad_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida")
        return

    if flor not in inventario:
        messagebox.showerror("Error", f"{flor} no está disponible")
        return

    datos = inventario[flor]
    if cantidad > datos["cantidad"]:
        messagebox.showwarning("Stock insuficiente", "No hay suficiente cantidad disponible")
        return

    datos["cantidad"] -= cantidad
    datos["vendidas"] += cantidad
    venta = datos["precio"] * cantidad
    total_ganado += venta
    messagebox.showinfo("Venta realizada", f"Vendidas {cantidad} de {flor} por ${venta}")

    if datos["cantidad"] == 0:
        del inventario[flor]
        actualizar_menu()


def añadir_flor():
    nombre = nueva_flor_entry.get().strip().lower()
    try:
        precio = int(precio_entry.get())
        cantidad = int(cantidad_nueva_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Precio o cantidad inválidos")
        return

    if nombre in inventario:
        messagebox.showwarning("Ya existe", "La flor ya está en el inventario")
        return

    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad,
        "vendidas": 0
    }
    actualizar_menu()
    messagebox.showinfo("Flor añadida", f"{nombre} añadida con éxito")


def eliminar_flor():
    flor = flor_var.get()
    if flor in inventario:
        del inventario[flor]
        actualizar_menu()
        messagebox.showinfo("Flor eliminada", f"{flor} fue eliminada del inventario")


def mostrar_total_flores():
    if not inventario:
        messagebox.showinfo("Inventario", "No hay flores en el almacén.")
        return

    total = sum(datos["cantidad"] for datos in inventario.values())
    detalle = "\n".join([
        f"{flor.title()}: {datos['cantidad']} unidades - ${datos['precio']} c/u"
        for flor, datos in inventario.items()
    ])
    mensaje = f"Total de flores en almacén: {total} unidades\n\nDetalle:\n{detalle}"
    messagebox.showinfo("Inventario total", mensaje)


def actualizar_menu():
    flor_menu['menu'].delete(0, 'end')
    for flor in inventario:
        flor_menu['menu'].add_command(label=flor, command=tk._setit(flor_var, flor))
    flor_var.set(next(iter(inventario), ""))


def cerrar_tienda():
    if not inventario:
        messagebox.showinfo("Resumen", "Todas las flores fueron vendidas.")
        return

    flores_vendidas = {flor: datos["vendidas"] for flor, datos in inventario.items()}
    mas_vendida = max(flores_vendidas, key=flores_vendidas.get)
    menos_vendida = min(flores_vendidas, key=flores_vendidas.get)

    resumen = (
        f"Total ganado: ${total_ganado}\n"
        f"Flor más vendida: {mas_vendida} ({flores_vendidas[mas_vendida]} unidades)\n"
        f"Flor menos vendida: {menos_vendida} ({flores_vendidas[menos_vendida]} unidades)"
    )
    messagebox.showinfo("Resumen de ventas", resumen)


ventana = tk.Tk()
ventana.title("Florería Mágica")

tk.Label(ventana, text="Bienvenido a la Florería Mágica 🌸", font=("Arial", 16)).pack(pady=10)


flor_var = tk.StringVar()
flor_var.set(next(iter(inventario)))
tk.Label(ventana, text="Selecciona una flor:").pack()
flor_menu = tk.OptionMenu(ventana, flor_var, *inventario.keys())
flor_menu.pack()

tk.Label(ventana, text="Cantidad a vender:").pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()


tk.Button(ventana, text="Vender", command=vender).pack(pady=5)
tk.Button(ventana, text="Eliminar flor seleccionada", command=eliminar_flor).pack(pady=5)


tk.Button(ventana, text="Ver total de flores en almacén", command=mostrar_total_flores).pack(pady=5)


tk.Label(ventana, text="Añadir nueva flor al inventario").pack(pady=10)
tk.Label(ventana, text="Nombre de la flor:").pack()
nueva_flor_entry = tk.Entry(ventana)
nueva_flor_entry.pack()

tk.Label(ventana, text="Precio:").pack()
precio_entry = tk.Entry(ventana)
precio_entry.pack()

tk.Label(ventana, text="Cantidad:").pack()
cantidad_nueva_entry = tk.Entry(ventana)
cantidad_nueva_entry.pack()

tk.Button(ventana, text="Añadir flor", command=añadir_flor).pack(pady=5)


tk.Button(ventana, text="Cerrar tienda", command=cerrar_tienda).pack(pady=10)

ventana.mainloop()
