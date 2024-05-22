
from simpleai.search import (
    SearchProblem,
    breadth_first,
    uniform_cost,
    depth_first,
    limited_depth_first,
    iterative_limited_depth_first,
    greedy,
    astar,
) # Este problema es igual que el tour del caballo, por lo que en vez de llevar una lista con las casillas y su respectivo color podemos llevar simplemente la casilla actual y una lista con las casillas visitadas, pero lo hago asi para variar
INITIAL = ((0,0),(((0,0),"rojo"),((0,1),"blanco"),((0,2),"blanco"),((0,3),"blanco"),((1,0),"blanco"),((1,1),"blanco"),((1,2),"blanco"),((1,3),"blanco"),((2,0),"blanco"),((2,1),"blanco"),((2,2),"blanco"),((2,3),"blanco"),))
from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer
class CaballoYPintura(SearchProblem):
    def actions(self, state):
        pos_actual, casillas = state
        actions = []
        posibilidades = []  # Genero las 8 casillas a las que se debería poder mover
        posibilidades.append((pos_actual[0] + 1, pos_actual[1] + 2))
        posibilidades.append((pos_actual[0] + 2, pos_actual[1] + 1))
        posibilidades.append((pos_actual[0] - 1, pos_actual[1] + 2))
        posibilidades.append((pos_actual[0] + 1, pos_actual[1] - 2))
        posibilidades.append((pos_actual[0] - 1, pos_actual[1] - 2))
        posibilidades.append((pos_actual[0] + 2, pos_actual[1] - 1))
        posibilidades.append((pos_actual[0] - 2, pos_actual[1] - 1))
        for x, y in posibilidades:  # Aca voy a suprimir las casillas ya visitadas y las casillas que están fuera del rango del tablero
            if (0 <= x <= 2 and 0 <= y <= 3 and ((x, y, "blanco") in casillas)):
                actions.append(((x, y), "blanco"))
        return actions

    def result(self, state, action): ##Voy a mover la casilla actual a la de la accion y pintar de rojo
        coord_actual = list(state[0])
        casillas = list(state[1])
        indice = casillas.index(action)
        coord_actual = action
        casillas[indice] = list(casillas[indice])
        casillas[indice][1] = "rojo"
        casillas[indice] = tuple(casillas[indice])
        state = list(state)
        state[0]= tuple(coord_actual)
        state[1] = tuple(casillas)  
        return tuple(state) 
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        goal = True
        for item in state[1]:
            if  "blanco" in item:
                goal = False
        return goal
    def heuristic(self, state):
        return 0
my_problem = CaballoYPintura(INITIAL)
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