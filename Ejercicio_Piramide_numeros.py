import itertools
from simpleai.search import CspProblem, backtrack

variables = [ 
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]
disponibles = list(range(1, 51))
dominio = {
    "0": 5,
    "1": 8,
    "2": disponibles,
    "3": 3,
    "4": disponibles,
    "5": disponibles,
    "6": disponibles,
    "7": disponibles,
    "8": disponibles,
    "9": 48
}

restricciones = []

def sumado(variables, valores):
    v1, v2, result = valores
    resultado = v1 + v2
    return result == resultado

restricciones.append(((variables[0], variables[1], variables[4]), sumado))
restricciones.append(((variables[1], variables[2], variables[5]), sumado))
restricciones.append(((variables[2], variables[3], variables[6]), sumado))
restricciones.append(((variables[4], variables[5], variables[7]), sumado))
restricciones.append(((variables[5], variables[6], variables[8]), sumado))
restricciones.append(((variables[7], variables[8], variables[9]), sumado))

def alldif(variables, valores):
    v1, v2 = valores
    if v1 == v2:
        return False
    else:
        return True

for val1, val2 in itertools.combinations(variables, 2):
    restricciones.append(((val1, val2), alldif))

problema = CspProblem(variables, dominio, restricciones)
solucion = backtrack(problema)

# Imprimir la solución
for i in range(1, 10):
    fila = [(i, j) for j in range(1, i+1)]
    for casillero in fila:
        print(solucion[casillero], end=" ")
    print()
