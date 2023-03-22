import json;
class Json:
    def __init__(self,file):
        self.file=file;
        self.file;
    def __str__(self) -> str:
        pass;

    def guardar(self,lista=None):
        with open(self.file, "w") as file:
            json.dump(lista,file,indent=4)

    def cargar(self):
        with open(self.file, "r") as file:
            p = file.read()
            if p != "":
                return json.loads(p);

if __name__ == "__main__":
    var = Json("prueba.json");
    var.guardar();
    if var.cargar() != None:
        print(var.cargar());