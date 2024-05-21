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

INITIAL = (500, (10, 30, 60, 80, 120, "linterna"), ())
GOAL = ( 10, 30, 60, 80, 120, "linterna")
class ProblemaDelPuente(SearchProblem):
    def actions(self,state):
        tiempo_linterna, lado_origen, lado_destino = state
        acciones = set()
        if "linterna" in lado_origen:
            for persona1 in lado_origen:
                for persona2 in lado_origen:
                    if persona1 != persona2 and persona1 != "linterna" and persona2 != "linterna":
                        # Añadir los pares en orden consistente para evitar duplicados
                        acciones.add(tuple(sorted((persona1, persona2))))
        else:
            for persona in lado_destino:
                if persona != "linterna":
                    acciones.add(persona,)
        return list(acciones)
    
    def result(self, state, action):
        tiempo_linterna, lado_origen, lado_destino = state
        lado_origen = list(lado_origen)
        lado_destino = list(lado_destino)

        if isinstance(action, (list, tuple)) and len(action) == 2:
            persona1, persona2 = action
            lado_destino.append(persona1)
            lado_destino.append(persona2)
            lado_destino.append("linterna")
            lado_origen.remove(persona1)
            lado_origen.remove(persona2)
            lado_origen.remove("linterna")
            tiempo_linterna -= max(persona1, persona2)
        else:
            persona1 = action
            lado_origen.append(persona1)
            lado_origen.append("linterna")
            lado_destino.remove(persona1)
            lado_destino.remove("linterna")
            tiempo_linterna -= persona1
        state = list(state)
        state[0] = tiempo_linterna
        state[1] = tuple(lado_origen)
        state[2] = tuple(lado_destino)
        state = tuple(state)
        return state
    
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        return (state[0] > 0) and (set(state[2]) == set(GOAL))

    def heuristic(self, state):
        return len(state[1])
my_problem = ProblemaDelPuente(INITIAL)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem,  viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)
