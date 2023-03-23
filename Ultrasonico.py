import pymongo
from pymongo import MongoClient
import RPi.GPIO as GPIO
import time

# Conexión con MongoDB
client = MongoClient('mongodb+srv://admin:12345@cluster0.lksnws1.mongodb.net/?retryWrites=true&w=majority')
db = client['DATOS']
collection = db['DATOS']

class Ultrasonico:
    def leer(self):
        TRIG = 23
        ECHO = 24

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        data = {
            'tipo': 'ultrasonico',
            'valor': 0,
            'fecha': time.strftime('%Y-%m-%d %H:%M:%S')
        }

        # Enviamos el pulso ultrasónico
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # Esperamos a que el pin ECHO se ponga en alto y medimos el tiempo
        while GPIO.input(ECHO) == GPIO.LOW:
            pulso_inicio = time.time()
        while GPIO.input(ECHO) == GPIO.HIGH:
            pulso_fin = time.time()

        # Calculamos la duración y la distancia
        duracion = pulso_fin - pulso_inicio
        distancia = (34300 * duracion) / 2

        # Actualizamos el valor en el diccionario y lo subimos a la base de datos
        data['valor'] = distancia
        print("Distancia: %.2f cm" % distancia)

        if client.server_info()['ok']:
            collection.insert_one(data)
        else:
            print("No hay conexión con la base de datos")

        # Limpiamos los GPIO
        GPIO.cleanup()
