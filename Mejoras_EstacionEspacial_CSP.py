import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

variables = [
    "sl1", "sl2", "sl3"
]

posibilidades = [
    "Baterias",
    "Brazo Robotico",
    "Ventana",
    "Antena",
    "Laboratorio plantas",
    "Laboratorio fisica",
    "Computadora de control",
    "Reciclador" 
]

mejoras = {
    "Baterias": [12.5, 300],
    "Brazo Robotico": [60, 50],
    "Ventana": [100, 550],
    "Antena": [20, 30],
    "Laboratorio plantas": [80, 250],
    "Laboratorio fisica": [75, 300],
    "Computadora de control": [50, 20],
    "Reciclador": [30, 100]
}

restricciones = []

def un_solo_lab(variables, valores):
    asignadas = set(valores)
    mal = set(("Laboratorio plantas", "Laboratorio fisica"))
    return asignadas == mal

def allfid(variables, valores):
    val1, val2 = valores
    return val1 != val2

def bateria_y_computadora(variables, valores):
    val1, val2 = valores
    if val1 == "Computadora de control" or val2 == "Computadora de control":
        if val1 != "Baterias" and val2 != "Baterias":
            return False
    return True

def menos_de_1_ton(variables, valores):
    peso = sum(mejoras[val][1] for val in valores)
    return peso <= 1000

def menos_de_150MM(variables, valores):
    costo = sum(mejoras[val][0] for val in valores)
    return costo <= 150

for v1, v2 in itertools.combinations(variables, 2):
    restricciones.append(((v1, v2), un_solo_lab))
    restricciones.append(((v1, v2), bateria_y_computadora))
    restricciones.append(((v1, v2), allfid))

restricciones.append((variables, menos_de_1_ton))
restricciones.append((variables, menos_de_150MM))

dominio = {var: posibilidades for var in variables}

problema = CspProblem(variables, dominio, restricciones)
solucion = min_conflicts(problema)

if solucion:
    print("Solución encontrada:", solucion)
else:
    print("No se encontró solución.")

