from pymongo import MongoClient
import json

class mongodb2:
    def __init__(self):
        try:
            cliente = MongoClient("mongodb+srv://admin:12345@cluster0.lksnws1.mongodb.net/?retryWrites=true&w=majority")
            db = cliente['DATOS']
            coleccion = db['DATOS']
            for producto in self.productos.lista:
                coleccion.insert_one(producto.__dict__)
            print("Productos agregados a MongoDB")

            # Actualizar cada documento con el valor de distancia correspondiente
            productos_coleccion = db['DATOS']
            for producto in self.productos.lista:
                codigo = producto.codigo
                distancia = productos_coleccion.find_one({'codigo': codigo})['distancia']
                producto.distancia = distancia
                # Insertar el documento actualizado en la misma colección
                productos_coleccion.replace_one({'codigo': codigo}, producto.__dict__)

            print("Distancias actualizadas en MongoDB")

        except:
            print("Error al conectar a la base de datos")
