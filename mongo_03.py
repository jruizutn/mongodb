"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 1-2023
Document.....: mongo_03.py
Goals........: Connection with mongoDB, CRUD data demonstration
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""

# Libraries required, may be you run pip install pymongo in your system
import os
import random
from subrutinas import *
import pymongo
import datetime

# Create connection
conex = pymongo.MongoClient(host=['10.236.2.142:27017'], username='admin', password='parda99*')

# Select database
db = conex.testing

#insert into tabla() values(),(),(),()

"""
# Create a collection data
db.categorias.insert_many([{"_id": 1,
                            "nombre": "Bebidas",
                            "descripcion": "Frescos, cafés, cervezas, licores"},

                           {"_id": 2,
                            "nombre": "Bocas",
                            "descripcion": "Entremes, platos pequeños, regalías"},

                           {"_id": 3,
                            "nombre": "Plato Fuertes",
                            "descripcion": "Plato completo para una persona"},

                           {"_id": 4,
                            "nombre": "Surtidos",
                            "descripcion": "Plato con varias porciones de 2 a mas personas"}])



# Update data
try:
    docus = db.categorias.find_one({'_id': 4})

    resu = db.categorias.update_one({'_id': docus['_id']},
                                    {'$set': {'descripcion': 'Platos para grupos de personas'}})
except Exception as e:
    print("Error: {0} {1}".format(type(e), e))



# Delete data
try:
    docus = db.categorias.find_one({'_id': 4})
    resu = db.categorias.delete_one({'_id': docus['_id']})
except Exception as e:
    print("Error: {0} {1}".format(type(e), e))

"""
db.productos.insert_many([{"_id": 1,
                           "nombre": "Heineken",
                           "descripcion": "Cerveza 365 mil",
                           "precio": 1000,
                           "categoria": 1},

                          {"_id": 2,
                           "nombre": "Ceviche pescado",
                           "descripcion": "Picadura pescado 124 gramos",
                           "precio":2800,
                           "categoria": 2},

                          {"_id": 3,
                           "nombre": "Ceviche cambute",
                           "descripcion": "Picadura cambute 250 gramos",
                           "precio": 1500,
                           "categoria": 2}])

try:
    docus = db.categorias.aggregate([
        {
            '$lookup': {
                'from': 'productos',
                'localField': '_id',
                'foreignField': 'categoria',
                'as': 'productos'
            }
        }
    ])

    for collect in docus:
        print("Categoría...: {0}".format(collect['nombre']))
        print("Descripción.: {0}".format(collect['descripcion']))
        print("====================================================")
        print('{0:>3} | {1:<15} | {2:>5}'.format('id','producto','precio'))
        for collect2 in collect['productos']:
            print('{0:>3} | {1:<15} | {2:>5}'.format(collect2['_id'], collect2['nombre'], collect2['precio']))
        print('\n\n')
except Exception as e:
    print("Error: {0} {1}".format(type(e), e))

