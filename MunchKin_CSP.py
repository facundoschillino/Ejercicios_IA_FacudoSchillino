from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)
import itertools

variables = ["Arma", "Armadura", "Pocion"]

dominio = {
    "Arma": ["EspadaMadera", "EspadaHierro", "EspadaAcero", "GarroteMadera"],
    "Armadura": ["Madera", "Hierro", "Acero"],
    "Pocion": ["Fuego", "Hielo", "Veneno"]
}

Costos = {
    "EspadaMadera": 1000,
    "EspadaHierro": 700,
    "EspadaAcero": 1000,
    "GarroteMadera": 1300,
    "Madera": 800,
    "Hierro": 1000,
    "Acero": 1300,
    "Fuego": 1500,
    "Hielo": 1100,
    "Veneno": 1000
}

Puntajes = {
    "EspadaMadera": 1,
    "EspadaHierro": 2,
    "EspadaAcero": 1,
    "GarroteMadera": 6,
    "Madera": 1,
    "Hierro": 3,
    "Acero": 5,
    "Fuego": 5,
    "Hielo": 2,
    "Veneno": 3
}



restricciones = []

def solo3000ysuman8(variables, valores):
    arma, armadura, pocion = valores
    totalCosto = Costos[arma] + Costos[armadura] + Costos[pocion]
    totalPuntos = Puntajes[arma] + Puntajes[armadura] + Puntajes[pocion]
    return (totalCosto <= 3000 and totalPuntos > 8)

restricciones.append((variables, solo3000ysuman8))

def fuego_vs_madera(variables, valores):
    val1, val2 = valores
    if ("Madera" in val1 or "Madera" in val2) and ("Fuego" in val1 or "Fuego" in val2):
        return False
    return True

for val1, val2 in itertools.combinations(variables, 2):
    restricciones.append(((val1, val2), fuego_vs_madera))

problema = CspProblem(variables, dominio, restricciones)
solucion = min_conflicts(problema)

print("Solución encontrada:", solucion)
    



