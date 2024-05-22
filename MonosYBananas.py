
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
hab_size_fila = 6
hab_size_colum = 6
INITIAL = (("Posicion_mono"),("Posicion_Silla"),("Lista_bananas"))
from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer

def esta_cerca (mono,silla): #Para ver si el mono se puede subir a la silla
    alrededor = []
    alrededor.append((silla[0]+1, silla[1]))
    alrededor.append((silla[0]-1, silla[1]))
    alrededor.append((silla[0], silla[1]+1))
    alrededor.append((silla[0], silla[1]-1))
    return (mono in alrededor)
class MonosyBananas(SearchProblem):
    def actions(self, state):
        actions = [] #Las acciones pueden ser mover la silla, subirse, o comer las bananas
        mono , silla, bananas = state
        if (silla in bananas): #Si la silla esta debajo de una banana
            cerca = esta_cerca(mono,silla)
            if cerca(mono, silla):
                actions.append("Comer", silla) #La voy a usar para sacar la banana de la lista
            else:
                actions.append("Moverse", (mono[0]+1, mono[1]))
                actions.append("Moverse", (mono[0]-1, mono[1]))
                actions.append("Moverse", (mono[0], mono[1]+1))
                actions.append("Moverse", (mono[0], mono[1]-1))
        elif(mono == silla): #El mono esta encima de la silla y no hay ninguna banana
             actions.append("Bajarse", (mono[0]+1, mono[1]))
             actions.append("Bajarse", (mono[0]-1, mono[1]))
             actions.append("Bajarse", (mono[0], mono[1]+1))
             actions.append("Bajarse", (mono[0], mono[1]-1))
        elif (esta_cerca(mono,silla)): # Puede empujar la silla
            algo = 0 # Aca lo deje, me dio paja seguir
        return 0
    def result(self, state, action):
        return 
    def cost(self, state, action, state2):
        return 
    def is_goal(self, state):
        return
    def heuristic(self, state):
        return 
my_problem = MonosyBananas(INITIAL)
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