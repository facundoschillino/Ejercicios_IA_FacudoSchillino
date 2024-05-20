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
INITIAL = ((0,0),(0,0))
#Visitadas = [(0,0)] No hay que llevar variables globales
class Tour_Del_Caballo(SearchProblem): #Preguntar a fisa
    def actions(self,state):
        actions = []
        posibilidades = []
        pos_actual = state[0]
        Visitadas = state[1]
        posibilidades.append((pos_actual[0]+1, pos_actual[1]+2))
        posibilidades.append((pos_actual[0]+2, pos_actual[1]+1))
        posibilidades.append((pos_actual[0]-1, pos_actual[1]+2))
        posibilidades.append((pos_actual[0]+1, pos_actual[1]-2))
        posibilidades.append((pos_actual[0]-1, pos_actual[1]-2))
        posibilidades.append((pos_actual[0]+2, pos_actual[1]-1))
        posibilidades.append((pos_actual[0]-2, pos_actual[1]-1))
        for posibilidad in posibilidades:
            ya_paso = False
            if posibilidad in Visitadas:
                 ya_paso = True
            if (posibilidad[0]>=0 and posibilidad[0]<=8 and posibilidad[1] >=0 and posibilidad[1]<=8 and ya_paso == False): ## Tengo que verificar en las acciones que el caballo no pueda moverse a una casilla ya visitada?
                actions.append(posibilidad)
        return actions
    def result (self,state,action):
        state = list(state)
        Visitadas = state[1]
        state[0] = action
        state[1]= list(state[1])
        state[1].append(action)
        state[1]= tuple(state[1])
        return tuple(state)
    
    def is_goal(self,state):
        Visitadas = state[1]
        total = len(Visitadas)
        return(total== 64)
    
    def cost(self,state,action,state2):
        return 1
    
    def heuristic(self,state):
        return 64

my_problem = Tour_Del_Caballo(INITIAL)
#v = BaseViewer()
v=WebViewer()
#v = ConsoleViewer()
#result = breadth_first(my_problem)
#result = uniform_cost(my_problem)
#result = depth_first(my_problem, graph_search=True)
result = astar(my_problem)
#result = limited_depth_first(my_problem, 6, viewer=v)
#result = iterative_limited_depth_first(my_problem, viewer=v)


if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")

    print("Final cost:", result.cost)