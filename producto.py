from lista import Lista;
import os

class Producto(Lista):
    def __init__(self,codigo=None,nombre=None,descripcion=None,precio=0):
        self.codigo = codigo;
        self.nombre = nombre;
        self.descripcion = descripcion;
        self.precio = precio;
        super().__init__("productos.json");
    def __str__(self) -> str:
        return f"{self.codigo}{self.nombre}{self.descripcion}{self.precio}";

    def cargarDiccionarioALista(self):
        diccionario = self.cargar()       
        if type(diccionario) == list:
            for lista in diccionario:
                self.agregar(Producto(
                    lista["codigo"], lista["nombre"], lista["descripcion"], lista["precio"]));
        else:
            self.agregar(Producto(
                diccionario["codigo"], diccionario["nombre"], diccionario["descripcion"], diccionario["precio"]));

    def buscar(self):
        cod = input("Escribir el codigo de producto a buscar.... ");
        i=0;
        while i < len(self.lista):
            if self.lista[i].codigo == cod:
                return i;
            i+=1;
        return print("Producto no encontrado")

    def mostrar(self,cabezera):
        print(cabezera);
        for lista in self.lista:
            print(lista.codigo, "\t", lista.nombre, "\t",lista.descripcion, "\t", lista.precio);
            
    def cabezera(self):
        return  "Codigo\t\tNombre\t\tDescripcion\t\tPrecio";

    def guardar(self):
        if len(self.lista) > 1:
            temporal = [];
            for li in self.lista:
                temporal.append(li.__dict__)
        else:
            temporal=self.lista[0].__dict__
        return super().guardar(temporal)






if __name__ == '__main__':
    productos = Producto();
    #Agregando Productos
   # productos.agregar(Producto("001","nose","desc..",121));
    #productos.agregar(Producto("001","nose","desc..",121));
    #productos.agregar(Producto("001","nose","desc..",121));
    print("Productos Guardadoa en Archivo .json");
    productos.guardar();