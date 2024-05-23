import itertools

from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)

variables = list(range(1,9))


variab = ("P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8")
dominios = {}
posibilidades = {
    'motor': [7,8],
    'ocultamiento': [1, 2, 3, 5],
    'apuntamiento': [1, 2, 3, 4],
    'torpedos': [1, 2],
    'medica': [5, 6, 7, 8],
    'mejorada': [5, 6],
    'escudo': variables,
    'comunicacion': variables,
    'evasion': [7, 8]}
doms = {}
INTERCONECTADAS = {
    1: [2, 3],
    2: [1, 3],
    3: [2, 1],
    4: [],
    5: [6],
    6: [5],
    7: [8],
    8: [7],
}

def diferentes (variables, valores): #No pueden repetirse mejoras, por lo que deben ser diferentes todas
    for var1,var2 in valores:
        if (var1 == var2):
            return False
        else:
            return True
def ocultamiento_vs_motor (variables, valores): #Si hay ocultamiento, no puede haber motor
    return not ('motor' in valores and 'ocultamiento' in valores)

def torpedo_with_apuntamiento(variables, valores): #En este metodo voy a revisar que esten ambas, y que esten conectadas
    if ('torpedo' in valores and 'apuntamiento' in valores):
        var1, var2 = variables
        if var2 not in INTERCONECTADAS[var1]:
            return False
    return True

def escudo_connected_with_comunicaciones(variables, valores):
    if 'escudo' in valores and 'comunicacion' in valores:
        var1, var2 = variables
        if var1 in INTERCONECTADAS[var2]:
            return False
    return True




PARTES ()