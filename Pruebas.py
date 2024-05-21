from simpleai.search import (
    SearchProblem,
    astar,
)
from simpleai.search.viewers import ConsoleViewer

INITIAL = ((0, 0), [])

class TourDelCaballo(SearchProblem):
    def actions(self, state):
        pos_actual, visitadas = state
        movimientos = [
            (pos_actual[0] + 1, pos_actual[1] + 2),
            (pos_actual[0] + 2, pos_actual[1] + 1),
            (pos_actual[0] + 1, pos_actual[1] - 2),
            (pos_actual[0] + 2, pos_actual[1] - 1),
            (pos_actual[0] - 1, pos_actual[1] + 2),
            (pos_actual[0] - 2, pos_actual[1] + 1),
            (pos_actual[0] - 1, pos_actual[1] - 2),
            (pos_actual[0] - 2, pos_actual[1] - 1),
        ]
        acciones = []
        for movimiento in movimientos:
            if 0 <= movimiento[0] < 8 and 0 <= movimiento[1] < 8 and movimiento not in visitadas:
                acciones.append(movimiento)
        return acciones

    def result(self, state, action):
        pos_actual, visitadas = state
        nuevas_visitadas = visitadas.copy()
        nuevas_visitadas.append(pos_actual)
        return (action, nuevas_visitadas)

    def is_goal(self, state):
        return len(state[1]) == 64

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        return 0  # No necesitamos heurística

my_problem = TourDelCaballo(INITIAL)
v = ConsoleViewer()
result = astar(my_problem, viewer=v)

if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("Siguiente Movimiento:", action)
        print("Casillas Visitadas:")
        print(state[1])
    print("Costo Total:", result.cost)

