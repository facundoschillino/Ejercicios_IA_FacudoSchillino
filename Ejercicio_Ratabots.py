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
#5x5
GOAL = ((3,5),3, ()) ##Posicion a la que tiene que llegar, cantidad de comidas que tiene que adquirir, posicion de las comidas
Initial_state = ((3,5), 0, ((1,2),(3,4),(4,0))) ##Me conviene mas pensarlo como un diccionario donde tengo : Posicion, cantidades comidas, y comidas restantes.
Obstaculos = ((0,3),(0,5),(1,3),(1,1),(2,2),(2,4),(3,0),(4,1),(4,3),(4,5),(5,3))


class Ratabots(SearchProblem):
    def actions (self, state):
        actions = [] #creo la lista acciones
        posicion, comidas, comidas_restantes = state ##descuajeringamos
        fila, columna = posicion ##volvemos a descuajeringar, pero ahora las posiciones
        posibilidades = [] ## creamos una lista para anadir las posibles posiciones a las que se puede mover la ratta
        posibilidades.append((fila +1, columna)) #abajo
        posibilidades.append((fila -1, columna))#arriba
        posibilidades.append((fila, columna+1))#derecha
        posibilidades.append((fila, columna-1)) #izquierda
        for casilla in posibilidades:
            if (casilla[0] >= 0 and casilla[0] <= 5) and (casilla[1] >= 0 and casilla[1] <= 5): #Si esta dentro de los limites de la grilla.
                Hay_un_obstaculo = (casilla in Obstaculos) #si no es un obstaculo
                if Hay_un_obstaculo == False :
                    actions.append((posicion,casilla))#origen, destino
        return actions ##Consultar a fisa si debo considerar en las acciones comer, o si lo hago en el resultado cuando la rata esta encima de la casilla que posee la comida
    
    def result(self, state, action):
        origen, destino = action
        Comidas = state[2]
        state = list(state)
        state[2]= list(state[2])
        for pos,comida in enumerate(Comidas): ##Si hay una comida, la come
            es_comida = (comida == destino)
            if es_comida:
                state[2].remove(comida)
                state[1] +=1 
        state [0] = destino
        state[2]= tuple(state[2])
        state = tuple(state)
        return state
    
    def is_goal(self, state):
        return state == GOAL
    
    def cost(self, state, action, state2):
        return 1
    
    def heuristics(self, state):
        Comidas = state[2]
        comidas_por_encontrar = Comidas.count()
        return comidas_por_encontrar
        

my_problem = Ratabots(Initial_state)

v = BaseViewer()
#v = WebViewer()
result = astar(my_problem, 1000, viewer= v)

if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")

    print("Final cost:", result.cost)        