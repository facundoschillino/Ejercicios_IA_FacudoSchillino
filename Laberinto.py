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
INITIAL=(1)
RELACIONES_CASILLAS=((9),(3,7,6,5),(4,2,8),(3,8,21),(2),(5,2),(9,2),(10,3,4),(12,7,1),(8,15,11),(10),(9,14,17),(14,17,19),(13,12,17),(18,10,16),(15,20),(19,12,13),(15),(17,13,20),(16,19),(4))
##Las relaciones de las casillas son las casillas a las que se puede entrar desde la casilla en la que estoy actualmente. Se cual es cual porque estab ubicadas segun el indice Ej : La casilla 10 esta en la posicion (indice + 1)
from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer
class Laberinto(SearchProblem):
    def actions(self, state):
        posibilidades = RELACIONES_CASILLAS[state-1]
        acciones = []
        if isinstance(posibilidades, tuple):
            if len(posibilidades) > 1:
                for posibilidad in posibilidades: #Agrego todas las posibilidades para esa casilla
                    acciones.append(posibilidad)  
        else:
            acciones.append(posibilidades) #Solo agrego la unica opcion que hay     
        return acciones
    def result(self, state, action):
        
        state = action
        return state
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        return (state == 21)
    def heuristic(self, state):
        return 0
my_problem = Laberinto(INITIAL)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem, 1000, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(state, sep="\n")
    print("Final cost:", result.cost)