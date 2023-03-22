from interfacecliente import InterfaceCliente
from interfaceproducto import InterfaceProducto
from interfaceventa import InterfaceVenta
class Interface:
    def __init__(self) -> None:
        self.cli = InterfaceCliente();
        self.prod = InterfaceProducto();
        self.venta = InterfaceVenta();
    def menu(self):
        print("a)\tVentas\nb)\tClientes\nc)\tProductos");
        op = input("Esoja una opcion de la 'a' a la 'd'\t");
        if(op == 'a'):
            self.venta.menu();
            self.menu();
        elif(op == 'b'):
            self.cli.menu();
            self.menu();
        elif(op == 'c'):
            self.prod.menu();
            self.menu();
        else:
            print("Adios........")
            return;

if __name__ == '__main__':
    ip=Interface();
    ip.menu();
