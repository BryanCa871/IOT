from producto import Producto
from pymongo import MongoClient
from demo import mongodb2
from Ultrasonico import Ultrasonico, ultrasonico

class InterfaceProducto(mongodb2):
    def __init__(self) -> None:
        self.productos = Producto()
        self.cargar()
    def menu(self):
        while True:
            print("1. Agregar Producto")
            print("2. Modificar Producto")
            print("3. Eliminar Producto")
            print("4. Mostrar")
            print("5. salir")
            opcion = input("Elija una opcion")
            if opcion == "1":
                ultrasonico()
                self.guardar()
                self.mongodb()
            elif opcion == "2":
                self.modificar()
                self.guardar()
            elif opcion == "3":
                self.eliminar()
                self.guardar()
            elif opcion == "4":
                self.mostrar()
            elif opcion == "5":
                print("Gracias por usar el programa")
                break
            else:
                print("Opcion no valida")

#TRY Y CATCH SI LACONEXION A MONGO DB FUE EXITOSA AGREGAR SINO MANDAR ERROR

    def agregar(self):
        self.productos.agregar(Producto(input("Escribe el codigo "),
        input("Escribe el nombre "),input("Escribe la descripcion "),int(input("Escribe el precio "))))
        input("Producto agregado....  Presione Enter...")
        self.menu()

    def modificar(self):
        self.productos.modificar(self.productos.buscar(),Producto(input("Escribe el codigo "),
        input("Escribe el nombre "),input("Escribe la descripcion "),int(input("Escribe el precio "))))
        input("Producto modificado....  Presione Enter...")

    def eliminar(self):
        self.productos.eliminar(self.productos.buscar())
        input("Producto eliminado....  Presione Enter...")

    def mostrar(self):
        self.productos.mostrar(self.productos.cabezera())
        input("Presione Enter...")

    def mongodb(self):
        self.mo()

    def guardar(self):
        self.productos.guardar()

    def cargar(self):
        self.productos.cargarDiccionarioALista()

if __name__ == '__main__':
    ip=InterfaceProducto()
    ip.menu()