ARCHIVO = "inventario.txt"

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def to_linea(self):
        return f"{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def desde_linea(linea):
        nombre, cantidad, precio = linea.strip().split(",")
        return Producto(nombre, cantidad, precio)


class Inventario:

    def __init__(self):
        self.productos = {}
        self.cargar()

    def cargar(self):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        p = Producto.desde_linea(linea)
                        self.productos[p.nombre] = p
                    except:
                        print("Línea inválida ignorada")

            print("Inventario cargado")

        except FileNotFoundError:
            open(ARCHIVO, "w").close()
            print("Archivo creado")

        except PermissionError:
            print("Sin permisos")

    def guardar(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for p in self.productos.values():
                    f.write(p.to_linea())
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def agregar(self, nombre, cantidad, precio):
        self.productos[nombre] = Producto(nombre, cantidad, precio)
        if self.guardar():
            print("Producto agregado")

    def actualizar(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].cantidad = int(cantidad)
            self.productos[nombre].precio = float(precio)
            if self.guardar():
                print("Actualizado")
        else:
            print("No existe")

    def eliminar(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            if self.guardar():
                print("Eliminado")
        else:
            print("No encontrado")

    def mostrar(self):
        for p in self.productos.values():
            print(p.nombre, "|", p.cantidad, "|", p.precio)


def main():
    inv = Inventario()

    while True:
        print("\n1 Agregar")
        print("2 Actualizar")
        print("3 Eliminar")
        print("4 Mostrar")
        print("5 Salir")

        op = input("Opción: ")

        if op == "1":
            inv.agregar(input("Nombre: "), input("Cantidad: "), input("Precio: "))
        elif op == "2":
            inv.actualizar(input("Nombre: "), input("Cantidad: "), input("Precio: "))
        elif op == "3":
            inv.eliminar(input("Nombre: "))
        elif op == "4":
            inv.mostrar()
        elif op == "5":
            break

if __name__ == "__main__":
    main()
