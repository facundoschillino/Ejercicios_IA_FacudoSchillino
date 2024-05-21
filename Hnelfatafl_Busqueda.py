from simpleai.search import (
    SearchProblem,
    breadth_first,
    uniform_cost,
    depth_first,
    limited_depth_first,
    iterative_limited_depth_first,
    greedy,
    astar,
)
from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer

INITIAL = (3,3)
ENEMIES=((0,0),(0,1),(0,4),(1,4),(2,0),(3,1),(3,6),(0,4),(6,5),(6,3))
def Casillas_atacadas(lista):
    posibilidades = []
    for enemigo in lista:
        fila = enemigo[0]
        columna = enemigo[1]
        posibilidades.append((fila-1, columna))
        posibilidades.append((fila+1,columna))
        posibilidades.append((fila, columna+1))
        posibilidades.append((fila, columna-1))
    return posibilidades

class Hnefatafl(SearchProblem):
    def actions(self, state):
        actions = []
        atacadas = Casillas_atacadas(ENEMIES)
        fila,columna = state
        posibilidades = []
        posibilidades.append((fila-1, columna))
        posibilidades.append((fila+1,columna))
        posibilidades.append((fila, columna+1))
        posibilidades.append((fila, columna-1))
        for casilla in posibilidades:
            Esta_atacada = (casilla in atacadas)
            if (casilla[0] >= 0 and casilla[0] <= 6) and (casilla[1] >= 0 and casilla[1] <= 6) and(Esta_atacada == False):
                actions.append(casilla)
        return actions
    def result(self, state, action):
        state = list(state)
        state = action
        return tuple(state)
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        casilla_actual = state #Lo hago asi solamente para verlo mejor. Tengo que verificar que este en un vorde y que no este atacada la casilla
        atacadas = Casillas_atacadas(ENEMIES)
        esta_atacada = (casilla_actual in atacadas)
        meta = False
        if (esta_atacada == False) and (casilla_actual[0] == 0 or casilla_actual[0] == 6 or casilla_actual[1] == 6 or casilla_actual[1] == 0):
            meta = True
        return meta
    def heuristic(self, state):
        al_borde = [] # Lista para guardar todos los valores faltantes al borde del tablero . Si bien empieza en el medio, si se quiere emepzar desde otra posicion se puede usar (Para este ej no sirve)
        for value in state:
            al_borde.append(6-value)
            al_borde.append(value)
        return min(al_borde)
    

my_problem = Hnefatafl(INITIAL)
v = BaseViewer()
#v = WebViewer()
result = astar(my_problem, 1000, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)