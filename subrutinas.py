"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 1-2023
Document.....: subrutinas.py
Goals........: Create any functions to support create random data to flat or binary file.
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""
import random

def ponCeros(expre, tam):
    local = ''
    for i in range(tam-len(expre)):
        local = local + "0"
    return local + expre


def impLinea(tam, expre):
    for i in range(tam):
        print(expre, end='')
    print('')


def nombre():
    nombres = ["Ana","Alvaro","Adriana","Arturo","Alfonso","Andrea","Andres","Anete","Arelys","Armando","Antonio",
                "Bianka","Beverly","Bruno","Braulio","Beatriz","Bernarda",
                "Cesar","Carolina","Carmen","Carlos","Cindy","Camilo","Clemencia","Cecilia","Cristina",
                "Diego","Dunia","David","Debora","Deisi","Diana","Danilo","Damaris","Doris","Daniel",
                "Efraín","Elsa","Elena","Ever","Ernesto","Eduardo","Esgardo","Emilio","Eilin","Esteban","Estiven","Elizabeth","Eneida",
                "Fabiola","Fernando","Francisco","Francini","Félix","Federico","Fabricio","Filomena",
                "Gabriela","Gerardo","Giovanna","German","Grisel","Gabriel","Gustavo","Gilberto","Graciela",
                "Hector","Hellen","Huberth","Humberto","Hilda","Homero",
                "Ignacio","Indira","Irma","Ingrid","Isaías","Ivania","Ileana","Isac","Isidro",
                "Jorge","Joyce","Julia","Jessica","José","Julio","Jacinto","Jaime","Joel","Jairo","Jesenia","Júan","Jesús","Juana",
                "Karla","Karen","Katia","Kevin","Kenneth","Katerina","Keylor","Kenyi","Karina",
                "Lorena","Lorenzo","Lady","Luis","Laura","Lucía","Lourdes","Leopoldo","Licet","Leticia",
                "Mario","Mauricio","Melania","Marianela","Mercedes","Marcos","Merlina","Morticia","Mauren",
                "Nuria","Nestor","Nazaret","Nidia","Norman","Naomi","Nora",
                "Osvaldo","Orlando","Odir","Olga","Ofelia","Omar","Olger","Oscar",
                "Pedro","Pablo","Patricia","Priscila","Paula","Paola","Pericles","Paolo",
                "Raúl", "Roberto", "Rebeca","Rocío","René","Rosaura","Rosalía","Rosa","Romel","Ricardo","Rigoberto",
                "Sabrina", "Sergio", "Sonia","Samuel","Sandra","Silvio","Susana","Sebastían","Sandro","Silvia",
                "Tatiana","Teodóro", "Tania","Teresa","Tobías","Toni",
                "Úrsula", "Uriel", "Ulises",
                "Verónica","Vanesa","Valeria","Victor","Vilma",
                "Walter","Wilfrido","Wendy","William","Wenceslao","Wilgem","Wilberth","Willis",
                "Xiomara", "Ximena", "Xavier",
                "Yirlania","Yolanda","Yonan","Yehúdi","Yvone","Yurielka","Yuri","Yenori",
                "Zaida", "Zulema","Zoe","Zacarías","Zoraida","Zeidy"]
    return random.choice(nombres)


def apellido():
    apellidos = ["Alvarado", "Almengor", "Acevedo", "Abarca", "Angulo", "Acón", "Apuy", "Artiaga", "Alvares",
                   "Ballesteros", "Barahona", "Barboza", "Blanco", "Bolaños", "Bermudez",
                   "Caballero", "Cespedes", "Campos", "Chavarría", "Cubero", "Cernas", "Cubillo", "Cambronero",
                   "Cabalceta", "Cortes", "Con",
                   "Duarte", "Durán", "Domingues", "De la O", "Díaz",
                   "Elizondo", "Echandi", "Escalante", "Espinoza", "Esquivel", "Estupiñan",
                   "Fernández", "Fonseca", "Fournier", "Fajardo", "Flores", "Fuentes",
                   "González", "Gaitan", "Galan", "Gambóa", "García",
                   "Hernández", "Herrera", "Hidalgo", "Huertas", "Hurtado",
                   "Ibarra", "Ibanéz", "Iglesias", "Infante", "Izaguirre",
                   "Jerez", "Jaén", "Jiménez", "Jácamo", "Juárez",
                   "López", "Lamas", "Lagos", "Labrador", "Lara", "Lí", "Leitón",
                   "Madrigal", "Molina", "Mendez", "Manzanares", "Monestel", "Molinares", "Matarrita", "Mata",
                   "Nuñez", "Noguera", "Naranjo", "Navas", "Nicolas",
                   "Ocampo", "Obregón", "Ochoa", "Ojeda", "Ordoñez",
                   "Pacheco", "Palacios", "Palma", "Padilla", "Paniagua", "Pomares",
                   "Quirós", "Quintero", "Quintana", "Quiroga", "Quintanilla",
                   "Ruiz", "Ramírez", "Roldan", "Redondo", "Rivera", "Rodriguez",
                   "Saborío", "Sanchez", "Salas", "Sáenz", "Sancho", "Sanabría", "Soto", "Sequeira", "Sibaja",
                   "Talavera", "Tenorio", "Trujillo", "Tijerino", "Torres",
                   "Ulloa", "Ugalde", "Ureña", "Urbina", "Ugarte",
                   "Vega", "Vargas", "Valencia", "Vallejo", "Varela", "Vizcaíno", "Valdez",
                   "Williams", "Wright", "Wong",
                   "Zamora", "Zarate", "Zumbado"]
    return random.choice(apellidos)

def cedula():
    ced = str(random.randrange(8)+1)
    ced = ced + ponCeros(str(random.randrange(1000)), 4) + ponCeros(str(random.randrange(1000)), 4)
    return int(ced)


def sexo():
    sexo = ["F", "M", "O"]
    return random.choice(sexo)


def estCivil():
    est = ["S", "C", "D", "V", "U"]
    return random.choice(est)


def fecNac():
    # Calculate day between 1 and 31
    expre = ponCeros(str(random.randrange(31)+1), 2) + "/"

    # Calculate month between 1 and 12
    expre = expre + ponCeros(str(random.randrange(12) + 1), 2) + "/"

    # Calculate year since 1960 at today
    expre = expre + str(random.randrange(59) + 1960)

    return expre

