from Led import led as Led
from Ultrasonico import ultrasonico
from Temperatura import temperatura as temp
class interfaz:
    def __init__(self): 
        super().__init__()

    def led():
        Led.led()
    def ultrasonico():
        ultrasonico.leer()
    def temperatura():
        temp.temperatura()
        

    

if __name__=='__main__':
    res = 0
    while res != 4 :
        print("1-leer sensor ultrasonico")
        print("2-leer temperatura y humedad")
        print("3-prender o apagar un led")
        print("4-salir")
        res = input("Que deseas hacer?")
        res = int (res)
        if res == 1:
            interfaz.ultrasonico()
        elif res == 2:
            interfaz.temperatura()
        elif res == 3:
            interfaz.led()
        elif res == 4:
            print("Good bye!!!")
        else:
            print("Opcion invalida")