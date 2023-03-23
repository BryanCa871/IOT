from pymongo import MongoClient
import json

class mongodb2:
    def __init__(self):
        try:
            cliente = MongoClient("mongodb+srv://admin:12345@cluster0.lksnws1.mongodb.net/?retryWrites=true&w=majority")
            db = cliente['DATOS']
            coleccion = db['productos']
            for producto in self.productos.lista:
                coleccion.insert_one(producto.__dict__)
            print("Productos agregados a MongoDB")

        except:
            print("Error al conectar a la base de datos")
    
    def mo(self):    
        try:
            cliente = MongoClient("mongodb+srv://admin:12345@cluster0.lksnws1.mongodb.net/?retryWrites=true&w=majority")
            db = cliente['diccionario']
            coleccion = db['diccionario']
            for producto in self.productos.lista:
                coleccion.insert_one(producto.__dict__)
            print("Productos agregados a MongoDB")

        except:
            print("Error al conectar a la base de datos")