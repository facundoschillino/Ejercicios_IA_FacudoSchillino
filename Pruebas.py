from simpleai.search import (
    SearchProblem,
    astar,
)
from simpleai.search.viewers import BaseViewer

# Estado inicial y estado objetivo
INITIAL = (0, 0, 0)
GOAL = (5, 1, 8)

class NaveAlienigena(SearchProblem):
    def actions(self, state):
        # Definir las posibles acciones
        return [
            "rojo",
            "verde",
            "amarillo",
            "celeste"
        ]

    def result(self, state, action):
        state = list(state)  # Convertir el estado a una lista para modificarlo
        if action == "rojo":
            state[0] += 3
        elif action == "verde":
            state[0] -= 2
        elif action == "amarillo":
            state[0], state[1] = state[1], state[0]
        elif action == "celeste":
            state[1], state[2] = state[2], state[1]
        return tuple(state)  # Convertir el estado de nuevo a una tupla

    def cost(self, state, action, state2):
        return 1  # Todas las acciones tienen el mismo costo

    def is_goal(self, state):
        return state == GOAL  # Verificar si el estado actual es el objetivo

    def heuristic(self, state):
        # Heurística que suma las diferencias absolutas entre el estado actual y el objetivo
        return sum(abs(state[i] - GOAL[i]) for i in range(len(state)))

# Crear una instancia del problema
my_problem = NaveAlienigena(INITIAL)
v = BaseViewer()

# Ejecutar la búsqueda A*
result = astar(my_problem, viewer=v)

# Mostrar los resultados
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("Action:", action)
        print("State:", state)
    print("Final cost:", result.cost)

