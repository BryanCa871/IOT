from lista import Lista
class Cliente(Lista):
    def __init__(self,nombre=None,RFC=None,telefono=None):
        self.nombre = nombre
        self.RFC = RFC
        self.telefono = telefono
        super().__init__("clientes.json")

    def __str__(self) -> str:
        return f"{self.nombre}{self.RFC}{self.telefono}"

    def cargarDiccionarioALista(self):
        diccionario = self.cargar()
        if type(diccionario) == list:
            for lista in diccionario:
                self.agregar(Cliente(lista["nombre"], lista["RFC"], lista["telefono"]))
        else:
            self.agregar(Cliente(lista["nombre"], lista["RFC"], lista["telefono"]))

    def buscar(self):
        rfc = input("Escribir el RFC  ")
        i=0;
        while i < len(self.lista):
            if self.lista[i].RFC == rfc:
                return i
            i+=1;
        return "Cliente no encontrado"

    def mostrar(self,cabezera):
        print(cabezera)
        for lista in self.lista:
            print(lista.nombre, "\t", lista.RFC, "\t",lista.telefono)
            
    def cabezera(self):
        return  "Nombre\tRFC\tTelefono"

    def guardar(self):
        if len(self.lista) > 1:
            temporal = []
            for li in self.lista:
                temporal.append(li.__dict__)
        else:
            temporal=self.lista[0].__dict__
        return super().guardar(temporal)

if __name__ == '__main__':
    clientes = Cliente()
    #Agregando Clientes
    #clientes.agregar(Cliente("nombre","RFC1","873837739"));
    #clientes.agregar(Cliente("nombre","RFC2","873837739"));
    #clientes.agregar(Cliente("nombre","RFC3","873837739"));
    #clientes.agregar(Cliente("nombre","RFC4","873837739"));
    print("clientes Guardadoa en Archivo .json");
    clientes.guardar();
    print("Datos Cargados del Archivo .josn: ")
    print(clientes.cargarDiccionarioALista())
    print("Modificar Cliente")
    print(clientes.modificar(clientes.buscar(),Cliente(input("Escribe el nombre"),input("Escribe el RFC"),input("Escribe el telefono"))))
    print("clientes")
    print(clientes.mostrar(clientes.cabezera()))
    print("Elimina un cleinte")
    clientes.eliminar(clientes.buscar())
    print("clientes")
    print(clientes.mostrar(clientes.cabezera()))