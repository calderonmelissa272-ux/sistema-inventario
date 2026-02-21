# ==============================
# SISTEMA DE INVENTARIO PRO
# ==============================

ARCHIVO = "inventario.txt"


# ------------------------------
# CLASE PRODUCTO
# ------------------------------
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def guardar_linea(self):
        return f"{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def desde_linea(linea):
        nombre, cantidad, precio = linea.strip().split(",")
        return Producto(nombre, int(cantidad), float(precio))


# ------------------------------
# CLASE INVENTARIO
# ------------------------------
class Inventario:

    def __init__(self):
        self.productos = {}
        self.cargar()

    # Cargar datos del archivo
    def cargar(self):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        p = Producto.desde_linea(linea)
                        self.productos[p.nombre] = p
                    except:
                        print("⚠ Línea dañada ignorada")

            print("✔ Inventario cargado")

        except FileNotFoundError:
            open(ARCHIVO, "w").close()
            print("📁 Archivo creado automáticamente")

        except PermissionError:
            print("❌ Sin permisos para leer archivo")

    # Guardar datos en archivo
    def guardar(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(p.guardar_linea())
            return True

        except PermissionError:
            print("❌ Sin permisos para guardar")
            return False

        except Exception as e:
            print("❌ Error:", e)
            return False

    # Agregar producto
    def agregar(self, nombre, cantidad, precio):
        self.productos[nombre] = Producto(nombre, cantidad, precio)
        if self.guardar():
            print("✔ Producto agregado")

    # Actualizar producto
    def actualizar(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].cantidad = cantidad
            self.productos[nombre].precio = precio
            if self.guardar():
                print("✔ Producto actualizado")
        else:
            print("❌ No existe")

    # Eliminar producto
    def eliminar(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            if self.guardar():
                print("✔ Producto eliminado")
        else:
            print("❌ No encontrado")

    # Mostrar inventario
    def mostrar(self):
        if not self.productos:
            print("Inventario vacío")
            return

        print("\n------ INVENTARIO ------")
        for p in self.productos.values():
            print(f"{p.nombre:15} Cantidad:{p.cantidad:4}  Precio:${p.precio:.2f}")


# ------------------------------
# FUNCIONES DE VALIDACIÓN
# ------------------------------

def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except:
            print("Ingrese número válido")


def pedir_float(texto):
    while True:
        try:
            return float(input(texto))
        except:
            print("Ingrese número válido")


# ------------------------------
# MENÚ PRINCIPAL
# ------------------------------
def main():

    inv = Inventario()

    while True:

        print("\n===== SISTEMA INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_float("Precio: ")
            inv.agregar(nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre: ")
            cantidad = pedir_entero("Nueva cantidad: ")
            precio = pedir_float("Nuevo precio: ")
            inv.actualizar(nombre, cantidad, precio)

        elif opcion == "3":
            nombre = input("Nombre: ")
            inv.eliminar(nombre)

        elif opcion == "4":
            inv.mostrar()

        elif opcion == "5":
            print("👋 Programa finalizado")
            break

        else:
            print("Opción inválida")


# Ejecutar
if __name__ == "__main__":
    main()
