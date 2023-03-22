from venta import Venta
from cliente import Cliente
from producto import Producto
class InterfaceVenta:
    def __init__(self) -> None:
        self.ventas = Venta()
        self.clientes = Cliente()
        self.productos = Producto()
        self.cargar()
    def menu(self):
        while True:
            print("1 Agregar Venta")
            print("2 Modificar Venta")
            print("3 Eliminar Venta")
            print("4 Mostrar Ventas")
            print("5 Salir")
            opcion = input("Esoja una opcion ")
            if opcion == "1":
                self.agregar()
                self.guardar()
            elif opcion == "2":
                self.modificar()
                self.guardar()
            elif opcion == "3":
                self.eliminar()
                self.guardar()
            elif opcion == "4":
                self.mostrar()
            elif opcion == "5":
                print("SALIENDO")
                return
            else:
                print("Opcion no valida")


    def agregar(self):
        self.ventas.agregar(self._datos())

    def modificar(self):
        indice = self.ventas.buscar()
        if type(indice) == int:
            self.ventas.modificar(indice,self._datos())
            input("Venta modificado....  Presione Enter...")

    def eliminar(self):
        self.ventas.eliminar(self.ventas.buscar())
        input("Venta eliminado....  Presione Enter...")

    def mostrar(self):
        self.ventas.mostrar(self.ventas.cabezera())
        input("Presione Enter...")

    def guardar(self):
        self.ventas.guardar()

    def cargar(self):
        self.ventas.cargarDiccionarioALista()
        self.clientes.cargarDiccionarioALista()
        self.productos.cargarDiccionarioALista()

    def _datos(self):
        indiceCli = self.clientes.buscar()
        if type(indiceCli) == int:
            cli = self.clientes.lista[indiceCli]
            prd = Producto()
            op = "si"
            print("Agrega productos... ")
            while op == "si":
                indicePrd = self.productos.buscar()
                if type(indicePrd) == int:
                    prd.agregar(self.productos.lista[indicePrd])
                op = input("AGREGAR?  si/no...  ")
            return Venta(prd.lista,cli,input("Ingresa la fecha de la venta "))
        else:
            print("Cliente no encotrado...")
            self.menu();

if __name__ == '__main__':
    ip=InterfaceVenta()
    ip.menu()
