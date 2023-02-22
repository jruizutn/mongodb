"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 1-2023
Document.....: mongo_02.py
Goals........: Create queries on mongoDB
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""
"""
    In the next link https://docs.mongodb.com/manual/reference/operator/query/#query-selectors, 
    you can see any queries examples
"""

# Libraries required, may be you run pip install pymongo in your system
from subrutinas import *
import pymongo
from datetime import datetime

# Create connection
conex = pymongo.MongoClient(host=['10.236.2.142:27017'], username='admin', password='parda99*')

# Select database
db = conex.testing

# Query on persona2
def consulta_01():

    #Select * from tabla where filtro
    #select campo1, campo2, campo3 from tabla order by

    proyeccion = {"ubicacion.poblado": 1,
                  "cedula": 1,
                  "apellidos": 1,
                  "nombre": 1}

    filtro = {
        'ubicacion.provincia': 'Puntarenas',
        'ubicacion.canton': 'Puntarenas',
        'ubicacion.distrito': 'Chacarita'
    }

    orden = [("ubicacion.poblado", -1),
             ("apellidos", -1),
             ("nombre", -1)]

    docus = db.personas2.find(filtro, proyeccion).sort(orden)

    print('{0:<25}| {1:<12}| {2:<35}|'.format('Poblado', 'Cédula', 'Nombre'))
    print('-------------------------+-------------+------------------------------------+')
    for collect in docus:
        print('{0:<25}| {1:<12}| {2:<35}|'.format(collect['ubicacion']['poblado'],
                                                  collect['cedula'],
                                                  collect['apellidos'] + ' ' + collect['nombre']))
        print('-------------------------+-------------+------------------------------------+')


# Query on ubicaciones, using mongoDB equal expression
def consulta_02():
    docus = db.ubicaciones.find({"provincia": {"$eq": "Puntarenas"}})

    print('{0:<15} | {1:<18} | {2:<25} |'.format('Cantón', 'Distrito', 'Poblado'))
    print('----------------+--------------------+---------------------------+')
    for collect in docus:
        print('{0:<15} | {1:<18} | {2:<25} |'.format(collect['canton'], collect['distrito'], collect['poblado']))
        print('----------------+--------------------+---------------------------+')


def date_to_str(expr):
    return ponCeros(str(expr.day), 2) + '/' + ponCeros(str(expr.month), 2) + '/' + str(expr.year)


# Query on persona3, using mongoDB between expression (simulated), and
# order by fecnac
def consulta_03():
    fecIni = datetime(1970, 1, 1)
    fecFin = datetime(1979, 12, 31)

    # select id, nombre, ape1, ape2, fechnac
    # from estudiantes
    # where fechnac between '1998-01-01' and '2005-12-31'

    docus = db.personas2.find({'fecnac': {'$gte': fecIni, '$lt': fecFin}}).sort('fecnac', -1)
    print('{0:<12} | {1:<30} | {2:<12} |'.format('Cédula', 'Nombre', 'Nacido el'))
    print('-------------+--------------------------------+--------------+')
    for collect in docus:
        print('{0:<12} | {1:<30} | {2:<12} |'.format(collect['cedula'],
                                                     collect['apellidos'] + ' ' + collect['nombre'],
                                                     date_to_str(collect['fecnac'])))
        print('-------------+--------------------------------+--------------+')


#consulta_01()
#consulta_02()
#consulta_03()