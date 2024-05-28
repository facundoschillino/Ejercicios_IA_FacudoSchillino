import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)

variables = ["SL1", "SL2", "SL3"]


posibilidades = [
    "ASSCUI",
    "BUTAX",
    "CLOAK",
    "HYPERSTONE",
    "QUELLINGBLADE",
    "SHADOWBLADE",
    "VEILDISCORD"
]
dominio = {
    "SL1":posibilidades,
    "SL2":posibilidades,
    "SL3":posibilidades
}
regenera_vida = [
    "BUTAX",
    "VEILDISCORD"]
PRECIOS = {
    "ASSCUI": 5000,
    "BUTAX":4000,
    "CLOAK":500,
    "HYPERSTONE":2000,
    "QUELLINGBLADE":200,
    "SHADOWBLADE":3000,
    "VEILDISCORD":2000
}
restricciones = []

def QueNoSePaseDe6000(variables, valores):
    suma = 0
    for val in valores:
        suma += PRECIOS[val]
    return suma <=6000
restricciones.append(((variables),QueNoSePaseDe6000))

def Hyp_vs_ShadBlad(varaibles, valores):
    val1, val2 = valores
    if val1 == "HYPERSTONE" or val2 == "HYPERSTONE":
        if val1 == "SHADOWBLADE" or val2 == "SHADOWBLADE":
            return False
    return True

def Cloak_vs_Veil (varaibles, valores):
    val1, val2 = valores
    if val1 == "CLOAK" or val2 == "CLOAK":
        if val1 == "VEILDISCORD" or val2 == "VEILDISCORD":
            return False
    return True

def regeneracion(variables, valores):
    for item in valores:
        if item in regenera_vida:
            return True
    return False
restricciones.append((variables,regeneracion))
def alldif(variables, valores):
    for var1, var2 in itertools.combinations(valores, 2):
        if var1 == var2:
            return False
    return True

for v1,v2 in itertools.combinations(variables, 2):
    restricciones.append(((v1,v2),alldif))
    restricciones.append(((v1,v2),Cloak_vs_Veil))
    restricciones.append(((v1,v2),Hyp_vs_ShadBlad))

problema = CspProblem(variables, dominio, restricciones)
solucion = backtrack(problema)

print("Solución encontrada:", solucion)