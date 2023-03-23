import RPi.GPIO as GPIO
import time
class Led:
    def __init__(self): 
        super().__init__()
    def led():          
        pin = 12
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(pin, GPIO.LOW)
        res = ""
        while res != "si":
            print("1-Apagar led")
            print("2-Encender led")
            opcion = input("Que deseas hacer?")
            try:
                opcion = int (opcion)
            except:
                print("eso no es un numero")
            if opcion == 1:
                GPIO.output(pin, GPIO.LOW)
            elif opcion == 2:
                GPIO.output(pin, GPIO.HIGH)
            else:
                print("Opcion no valida")
            res = input("deseas salir?")

        GPIO.cleanup()
