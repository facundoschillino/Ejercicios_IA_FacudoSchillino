import itertools
from simpleai.search import CspProblem, backtrack

# Definición de variables
variables = [(n, i) for n in range(7) for i in range(7)]
posibilidades = ["REY", "SOLDADO", None]  # Agrego None para representar casillas vacías

# Definición del dominio
dominio = {var: posibilidades for var in variables}

# Lista para almacenar las restricciones
restricciones = []

# Restricción para que los reyes no tengan más de un rey adyacente
def nomasdeunadyacenteXD(variable, valores):
    fila, columna = variable
    valor = valores[variable]
    if valor == "REY":
        reyes_adyacentes = 0
        for delta_fila, delta_columna in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            vecino = (fila + delta_fila, columna + delta_columna)
            if vecino in valores and valores[vecino] == "REY":
                reyes_adyacentes += 1
        return reyes_adyacentes <= 1
    return True

# Añadir restricciones para cada celda
for variable in variables:
    restricciones.append(((variable,), nomasdeunadyacenteXD))

# Restricción para la cantidad de soldados y reyes
def massoldadosquereyes(variables, valores):
    reyes = sum(1 for valor in valores.values() if valor == "REY")
    soldados = sum(1 for valor in valores.values() if valor == "SOLDADO")
    return reyes == 0 or (soldados > reyes and soldados < reyes * 2)

restricciones.append((variables, massoldadosquereyes))

# Definición del problema CSP
problema = CspProblem(variables, dominio, restricciones)

# Resolver el problema utilizando backtrack
solucion = backtrack(problema)

# Mostrar la solución
print("Solución encontrada:")
for fila in range(7):
    for columna in range(7):
        print(solucion.get((fila, columna), None), end=" ")
    print()
