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
INITIAL = (0,0,0)
GOAL = (5,1,8)
class Nave_Alienigena(SearchProblem):
    def actions(self, state):
        actions = []
        actions.append(("rojo",3,0)) #Color del boton, lo que se resta, a que casilla
        actions.append(("verde", -2,0))  #Color del boton, lo que se resta, a que casilla
        actions.append(("amarillo", 0, 1))# Color, Origen y destino
        actions.append(("celeste",1,2))# Color, origen, destino     
        return actions
    def result(self, state, action):
        state = list(state)
        if (action[0] == "rojo" or action[0] == "verde"):
            color,cantidad,destino = action
            state[destino] += cantidad
        else:
            color, origen, destino = action
            state[origen], state[destino] = state[destino], state[origen]
        state = tuple(state)
        return state
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        return state == GOAL
    def heuristic(self, state):
        correctos = 0
        for index, item in enumerate(state):
            if GOAL[index] == item:
                correctos += 1
        return correctos
my_problem = Nave_Alienigena(INITIAL)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)