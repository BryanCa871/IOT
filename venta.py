from lista import Lista;
from producto import Producto;
from cliente import Cliente;
class Venta(Lista):
    def __init__(self,producto=None,cliente=None,fecha=""):
        self.producto = producto;
        self.cliente = cliente;
        self.fecha = fecha;
        super().__init__("ventas.json");
    def guardar(self):
        if len(self.lista) > 1:
            ventas=[];
            for li in self.lista:
                prd=[];
                for lo in li.producto:
                    prd.append(lo.__dict__);
                ventas.append(dict(cliente=li.cliente.__dict__,productos=prd,fecha=li.fecha));
        else:
            prd=[];
            for lo in self.lista[0].producto:
                prd.append(lo.__dict__);
            ventas = dict(cliente=self.lista[0].cliente.__dict__,productos=prd,fecha=self.lista[0].fecha);
        return super().guardar(ventas);

    def mostrar(self,cabezera):
        print(cabezera);
        for lista in self.lista:
            print(lista.cliente.nombre, "\t\t", len(lista.producto), "\t\t",lista.fecha);

    def cabezera(self):
        return  "Nombre\t\tProductos\t\tfecha";    

    def cargarDiccionarioALista(self):
        diccionario = self.cargar()       
        if type(diccionario) == list:
            for lista in diccionario:
                prd = Producto();
                for lis in lista['productos']:
                    prd.agregar(Producto(lis['codigo'],lis['nombre'],lis['descripcion'],lis['precio']));
                cli = Cliente(lista['cliente']["nombre"],lista['cliente']['RFC'],lista['cliente']['telefono']);
                self.agregar(Venta(prd.lista,cli,lista['fecha']));
        else:
            prd = Producto();
            for lis in diccionario['productos']:
                prd.agregar(Producto(lis['codigo'],lis['nombre'],lis['descripcion'],lis['precio']));
            cli = Cliente(diccionario['cliente']["nombre"],diccionario['cliente']['RFC'],diccionario['cliente']['telefono']);
            self.agregar(Venta(prd.lista,cli,diccionario['fecha']));
        
    def buscar(self):
            cod = input("Escribir la fecha de la venta a buscar.... ");
            i=0;
            while i < len(self.lista):
                if self.lista[i].fecha == cod:
                    return i;
                i+=1;
            return print("Venta no encontrada");

if __name__ == '__main__':
    productos = Lista();
    #productos.agregar(Producto("001","nose","desc..",121));
    #productos.agregar(Producto("002","nose2","desc..",123));
    #productos.agregar(Producto("004","nose3","desc..",122));
    #cliente = Cliente("Jose","JDOSJ20","829398928");
    venta = Venta();
    venta.mostrar(venta.cabezera());
    #venta.agregar(Venta(productos.lista,cliente,"12/12/12"));
    #venta.agregar(Venta(productos.lista,cliente,"12/12/13"));
    #venta.guardar();
    venta.cargarDiccionarioALista();
    venta.mostrar(venta.cabezera());
    venta.eliminar(venta.buscar());
    venta.guardar();
    venta.mostrar(venta.cabezera());