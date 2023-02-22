"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 1-2023
Document.....: mongo_04.py
Goals........: Demonstration
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""

# Libraries required, may be you run pip install pymongo in your system
import pymongo

# Create connection
conex = pymongo.MongoClient(host=['10.236.2.142:27017'], username='admin', password='parda99*')

# Select database
db = conex.negocio


# Insert example data
db.persona_3.insert_many([
    {
    "_id": 123,
    "nombre": "Morticia Addams"
    },
    {
    "_id": 456,
    "nombre": "Merlina Addams"
    }])

db.cliente.insert_one({
    "tCliente": "Ocacional",
    "aRegistro": 2018,
    "persona": 123
})

db.empleado.insert_one({
    "funcion": "Mesera",
    "experincia": "5 años servicio cliente",
    "cualidades": "3 idiomas, contabilidad básica",
    "persona": 456
})

db.factura.insert_one({
    "nFactura": "00012013",
    "fecha": "2020-08-30 13:45:00",
    "detalle": [
        ("1 Plato de pianguas vivas", 7500),
        ("1 Tartar de atún", 15000),
        ("1 Cocktail de camarones", 9000),
        ("3 Copas de vino blanco", 7500),
        ("6 Cervezas Stella Artois", 12000)
    ],
    "cliente": 123,
    "salonero": 456
})


docus = db.factura.aggregate([
    {
        '$lookup': {
            'from': 'persona_3',
            'localField': 'cliente',
            'foreignField': '_id',
            'as': 'cliente'
        }
    },
    {
            '$lookup': {
                'from': 'persona_3',
                'localField': 'salonero',
                'foreignField': '_id',
                'as': 'salonero'
            }
        }
    ])



# Only breakpoint use
print(docus)
