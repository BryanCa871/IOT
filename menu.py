from Ultrasonico import Ultrasonico

class Interfaz:
    def __init__(self):
        super().__init__()

    def led(self):
        Led.led()

    def ultrasonico(self):
        Ultrasonico().leer()

    def temperatura(self):
        temp.temperatura()

if __name__ == '__main__':
    res = 0
    while res != 4:
        print("1-leer sensor ultrasonico")
        print("2-leer temperatura y humedad")
        print("3-prender o apagar un led")
        print("4-salir")
        res = raw_input("Que deseas hacer?")
        res = int(res)
        if res == 1:
            Interfaz().ultrasonico()
        elif res == 2:
            Interfaz().temperatura()
        elif res == 3:
            Interfaz().led()
        elif res == 4:
            print("Good bye!!!")
        else:
            print("Opcion invalida")
