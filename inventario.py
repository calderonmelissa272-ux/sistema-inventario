# ==============================
# SISTEMA DE INVENTARIO AVANZADO
# Guarda productos en archivo
# Manejo de excepciones incluido
# ==============================

ARCHIVO = "inventario.txt"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_archivo()

    # -------------------------
    # CARGAR INVENTARIO
    # -------------------------
    def cargar_archivo(self):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    nombre, precio, cantidad = linea.strip().split(",")
                    self.productos[nombre] = {
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    }
            print("✔ Inventario cargado correctamente")

        except FileNotFoundError:
            # Si no existe, lo crea
            open(ARCHIVO, "w").close()
            print("⚠ Archivo inventario.txt creado")

        except Exception as e:
            print("❌ Error al leer archivo:", e)

    # -------------------------
    # GUARDAR INVENTARIO
    # -------------------------
    def guardar_archivo(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for nombre, datos in self.productos.items():
                    f.write(f"{nombre},{datos['precio']},{datos['cantidad']}\n")
            print("✔ Archivo actualizado")

        except PermissionError:
            print("❌ Sin permisos para escribir archivo")

        except Exception as e:
            print("❌ Error guardando:", e)

    # -------------------------
    # AGREGAR PRODUCTO
    # -------------------------
    def agregar(self):
        nombre = input("Nombre: ")

        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            self.productos[nombre] = {
                "precio": precio,
                "cantidad": cantidad
            }

            self.guardar_archivo()
            print("✔ Producto agregado")

        except ValueError:
            print("❌ Precio o cantidad inválidos")

    # -------------------------
    # MOSTRAR
    # -------------------------
    def mostrar(self):
        if not self.productos:
            print("Inventario vacío")
            return

        for n, d in self.productos.items():
            print(f"{n} | Precio: {d['precio']} | Cantidad: {d['cantidad']}")

    # -------------------------
    # ELIMINAR
    # -------------------------
    def eliminar(self):
        nombre = input("Producto a eliminar: ")

        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_archivo()
            print("✔ Eliminado")
        else:
            print("❌ No existe")


# ==============================
# MENU PRINCIPAL
# ==============================

def menu():
    inv = Inventario()

    while True:
        print("\n=== INVENTARIO ===")
        print("1 Agregar")
        print("2 Mostrar")
        print("3 Eliminar")
        print("4 Salir")

        op = input("Opción: ")

        if op == "1":
            inv.agregar()
        elif op == "2":
            inv.mostrar()
        elif op == "3":
            inv.eliminar()
        elif op == "4":
            print("Adiós")
            break
        else:
            print("Opción inválida")


menu()
