from cliente import Cliente
class InterfaceCliente:
    def __init__(self) -> None:
        self.clientes = Cliente();
        self.cargar();
    def menu(self):
        while True:
            print("1 Agregar Cliente")
            print("2 Modificar Cliente")
            print("3 Eliminar Cliente")
            print("4 Mostrar Clientes")
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
        self.clientes.agregar(Cliente(input("Escribe el nombre "),input("Escribe el RFC "),input("Escribe el numero de telefono ")))
        input("Cliente agregado....  Presione Enter...")
        self.menu()

    def modificar(self):
        self.clientes.modificar(self.clientes.buscar(),Cliente(input("Escribe el nombre "),input("Escribe el RFC "),input("Escribe el numero de telefono ")))
        input("Cliente modificado....  Presione Enter...")
        self.menu()

    def eliminar(self):
        self.clientes.eliminar(self.clientes.buscar())
        input("Cliente eliminado....  Presione Enter...")
        self.menu()

    def mostrar(self):
        self.clientes.mostrar(self.clientes.cabezera())
        input("Presione Enter...")
        self.menu()

    def guardar(self):
        self.clientes.guardar()

    def cargar(self):
        self.clientes.cargarDiccionarioALista()

if __name__ == '__main__':
    ip=InterfaceCliente()
    ip.menu()