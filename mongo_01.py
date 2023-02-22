"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 1-2023
Document.....: mongo_01.py
Goals........: Connection with mongoDB demonstration, insert data
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

# Select database or container
db = conex.testing

# Testing connection, print some data
print('Nombre de la base de datos: {0}'.format(db.name))
print('Colecciones actuales:')
print(db.my_collection)

# Create local array to store ubicaciones json
ubicaciones = []
ruta = 'D:/Documentos/Cursos UTN/2022 - 2/ITI-411/Material/data_c4'
os.chdir(ruta)


# Populate function, create many documents into personas container
def creaPersonas_1(nTuplas):
    try:
        for i in range(nTuplas):
            db.persona.insert_one({
                "cedula": str(cedula()),
                "nombre": nombre(),
                "apellidos": apellido()+' '+apellido(),
                "sexo": sexo(),
                "ecivil": estCivil(),
                "fecnac": fecNac()
            })
    except Exception as excp:
        print(excp)


# Populate function, create many documents into ubicaciones collection,
# from ubicaciones.csv file, separated values for semicolon ";"
def cargaUbicaciones():
        try:
            # Open file with only read mode and utf8 encoding
            archivo = open('ubicaciones.csv', mode='r', encoding='utf8')
            continua = True
            conta = 0

            # Read all lines
            while continua:
                linea = archivo.readline()
                if conta > 0:
                    if linea != '':
                        # Separate line into chunks
                        id, provincia, canton, distrito, poblado = linea.split(';')
                        db.ubicaciones.insert_one({
                            "_id": ponCeros(str(conta), 5),
                            "idubi": str(id),
                            "provincia": provincia,
                            "canton": canton,
                            "distrito": distrito,
                            "poblado": poblado.rstrip('\n')
                        })
                    else:
                        continua = False
                conta += 1

            # Close file
            archivo.close()
        except Exception as excp:
            print(print(excp))


# Populate function, create many documents into ubicaciones array
def cargaUbicaciones2():
        try:
            # Open file with only read mode and utf8 encoding
            archivo = open('ubicaciones.csv', mode='r', encoding='utf8')
            continua = True
            conta = 0

            # Read all lines
            while continua:
                linea = archivo.readline()
                if conta > 0:
                    if linea != '':
                        # Separate line into chunks
                        id, provincia, canton, distrito, poblado = linea.split(';')
                        ubicaciones.append({
                            "idubi": str(id),
                            "provincia": provincia,
                            "canton": canton,
                            "distrito": distrito,
                            "poblado": poblado.rstrip('\n')
                        })
                    else:
                        continua = False
                conta += 1

            # Close file
            archivo.close()
        except Exception as excp:
            print(print(excp))


# Populate function, create many documents into personas collection
# with embedded ubicacion documents
def creaPersonas_2(nTuplas):
    for i in range(nTuplas):
        try:
            db.personas2.insert_one({
                "cedula": str(cedula()),
                "nombre": nombre(),
                "apellidos": apellido()+' '+apellido(),
                "sexo": sexo(),
                "ecivil": estCivil(),
                "fecnac": datetime.datetime.strptime(fecNac(), '%d/%m/%Y'),
                "ubicacion": random.choice(ubicaciones)
            })
        except Exception as excp:
            print(excp)


# Call functions, to store data into database collections
#creaPersonas_1(1500)
#cargaUbicaciones()

# Call array populate
cargaUbicaciones2()

# Create second kind of persons
creaPersonas_2(1500)
