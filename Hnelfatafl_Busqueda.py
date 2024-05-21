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

class BusquedaDota(SearchProblem):
    def actions(self, state):
        actions = []
        posibilidades = Casillas_atacadas(ENEMIES)
        fila,columna = state
        posibilidades.append((fila-1, columna))
        posibilidades.append((fila+1,columna))
        posibilidades.append((fila, columna+1))
        posibilidades.append((fila, columna-1))
        for casilla in posibilidades:
            Esta_atacada = (casilla in posibilidades)
            if (casilla[0] >= 0 and casilla[0] <= 6) and (casilla[1] >= 0 and casilla[1] <= 6) and(Esta_atacada == False):
                actions.append(casilla)
        return actions
    def result(self, state, action):
        return 
    def cost(self, state, action, state2):
        return 
    def is_goal(self, state):
        return
    def heuristic(self, state):
        return 
my_problem = BusquedaDota(Initial_state)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem, 1000, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)