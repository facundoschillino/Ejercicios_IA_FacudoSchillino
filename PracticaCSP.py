import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)
variables = list(range(1,7))
dominio = {}
pos_disponibles = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4), (2,0), (2,1), (2,3), (2,4), (3,0), (3,1), (3,2), (3,3), (3,4)]
restringidas= ((0,2),(1,3),(2,1))
restricciones = []
puertas_exteriores = ((0,4),(3,2))
def alldif(variables, valores):
    for var1, var2 in itertools.combinations(valores, 2):
        if var1 == var2:
            return False
    return True

def no_adyacentes(variables, valores):
    posiciones = []
    val1, val2 = valores
    posiciones.append((val1[0]+1, val1[1]))
    posiciones.append((val1[0]-1, val1[1]))
    posiciones.append((val1[0], val1[1]+1))
    posiciones.append((val1[0], val1[1]-1))
    return val2 not in posiciones
    
    
def no_restringidas(variables, valores):
    for val in valores:
        if val in restringidas:
            return False
    return True



def in_puertas(variables, valores):
    contador = 0
    for val in valores:
        if val in puertas_exteriores:
            contador += 1
    return contador == 2

restricciones.append(((variables),in_puertas)) #aplica a todas
for val1, val2 in itertools.combinations(variables,2):
	restricciones.append(((val1,val2),alldif))
	restricciones.append(((val1,val2),no_adyacentes))
restricciones.append((variables, no_restringidas))
problema = CspProblem(variables, {var: pos_disponibles for var in variables}, restricciones)
# Resolución del problema usando backtracking
solucion = backtrack(problema)
print(solucion)