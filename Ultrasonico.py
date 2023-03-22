import RPi.GPIO as GPIO
import time
from pymongo import MongoClient

class Ultrasonico:
    def __init__(self):
        self.client = MongoClient('localhost', 27017) # Conectar con MongoDB
        self.db = self.client['datos'] # Elegir la base de datos
        self.collection = self.db['ultrasonido'] # Elegir la colección

    def leer(self):
        TRIG = 23 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor
        ECHO = 24 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor

        GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
        GPIO.setup(TRIG, GPIO.OUT) #Configuramos el pin TRIG como una salida 
        GPIO.setup(ECHO, GPIO.IN)  #Configuramos el pin ECHO como una salida 

        try:
            while True:
                GPIO.output(TRIG, GPIO.LOW)
                time.sleep(0.5)

                GPIO.output(TRIG, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(TRIG, GPIO.LOW)

                while True:
                    pulso_inicio = time.time()
                    if GPIO.input(ECHO) == GPIO.HIGH:
                        break

                while True:
                    pulso_fin = time.time()
                    if GPIO.input(ECHO) == GPIO.LOW:
                        break

                duracion = pulso_fin - pulso_inicio
                distancia = (34300 * duracion) / 2

                # Guardar los datos en MongoDB
                data = {'distancia': distancia, 'fecha': time.strftime("%Y-%m-%d %H:%M:%S")}
                self.collection.insert_one(data)

        except KeyboardInterrupt:
            GPIO.cleanup()

if __name__ == '__main__':
    sensor = Ultrasonico()
    sensor.leer()
