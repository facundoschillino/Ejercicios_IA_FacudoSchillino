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
from simpleai.search.viewers import BaseViewer, WebViewer
Dimension_tablero = (3,4)
Obstaculos = ((0,2),(2,1),(1,3))
Initial_state = ((0,1),(0,1))
GOAL = ((3,2),(0,4))
class Robots_Defensivos(SearchProblem):
    def actions(self, state):
        actions = []
        robot1,robot2= state
        robot1Fila, Robot1Columna = robot1
        robot2Fila, Robot2Columna = robot2
        posibilidades = [] ##hago una lista de las posibles opciones que tienen los robots para moverse
        posibilidades.append((1,robot1Fila-1, Robot1Columna))
        posibilidades.append((1,robot1Fila+1,Robot1Columna))
        posibilidades.append((1,robot1Fila, Robot1Columna+1))
        posibilidades.append((1,robot1Fila, Robot1Columna -1))
        posibilidades.append((2,robot2Fila-1, Robot2Columna))
        posibilidades.append((2,robot2Fila+1,Robot2Columna))
        posibilidades.append((2,robot2Fila, Robot2Columna+1))
        posibilidades.append((2,robot2Fila, Robot2Columna -1))
        for posible_casillero in posibilidades:
            if posible_casillero[0] >= 0 and posible_casillero [0] <= 3 and posible_casillero[1] >= 0 and posible_casillero [0] <= 4: #Si esta dentro del rango y no hay un obstaculo es una opción
                if (posible_casillero in Obstaculos) == False:
                    actions.append(posible_casillero)
        return actions
    def result(self, state, action):   
        que_robot_es = action[0]
        destino = (action[1], action[2])
        state = list(state)
        state[que_robot_es -1] = destino
        state = tuple(state)
        return state
    def is_goal(self, state):
        return state == GOAL
    def cost(self, state, action, state2):
        return 1
    def heuristics(self, state):
        cuanto_falta = 0
        for cual,robot in enumerate(state):
            objetivo = GOAL[cual]
            cuanto_falta = abs(robot[0] - objetivo[0])
            cuanto_falta = abs(robot[1] - objetivo[1])
        return cuanto_falta
my_problem = Robots_Defensivos(Initial_state)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem, 1000, viewer= v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")

    print("Final cost:", result.cost)    
            
 