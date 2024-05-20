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
Initial_state= (("heroe",(2,0)),("enemigo", (1,1)),("Base",(0,2)))
GOAL= (("heroe",(0,2)))
class BusquedaDota(SearchProblem):
    def actions(self, state):
        actions = []
        heroe = state[0]
        coordenadas_heroe = heroe[1]
        fila_coordenadas_heroe = coordenadas_heroe[0]
        columna_coordenadas_heroe = coordenadas_heroe[1]
        posibilidades = [] #aca guardo las posibles casillas a las que puede moverse o atacar
        coordenadas_villanos = [] ## lo hago así por si quiero agregar mas villanos al problema
        for villanos in state: #Verifico las coordenadas de los villanos en el tablero
            if "enemigo" in villanos or "Base" in villanos:
                coordenadas_villanos.append(villanos[1])
        posibilidades.append((fila_coordenadas_heroe-1, columna_coordenadas_heroe))
        posibilidades.append((fila_coordenadas_heroe+1,columna_coordenadas_heroe))
        posibilidades.append((fila_coordenadas_heroe, columna_coordenadas_heroe+1))
        posibilidades.append((fila_coordenadas_heroe, columna_coordenadas_heroe-1))
        for posicion_en_la_lista, posibilidad in enumerate(posibilidades):
            hay_villano = False
            if posibilidad in coordenadas_villanos:
                actions.append(("atacar", posicion_en_la_lista)) ##Como tengo que sacarlo, voy a anotarme el lugar del estado en el que está
                hay_villano = True
            if posibilidad[0] >=0 and posibilidad[0] <=2 and posibilidad[1]<=2 and posibilidad[1] >=0  and hay_villano == False:
                actions.append(("mover", posibilidad)) # aca si guardo la coordenada de destino
        return actions
    def result(self, state, action):
        accion, coordenadas_destino = action  ##pregunto cual es la accion que corresponde, y la coordenada
        state = list(state)
        heroe = list(state[0]) #saco al heroe
        if accion == "mover":
            heroe[1] = coordenadas_destino
            state[0] = heroe
        else:
            del state[coordenadas_destino]
        
        return tuple(state)
    def cost(self, state, action, state2):
        return 1
    def is_goal(self, state):
        return state == GOAL
    def heuristic(self, state):
        movimientos_restantes = 2 #Tengo como mínimo 2 movimientos por destruir la base, y por moverme a la casilla de la misma
        for item in state:
            if (item[0]== "enemigo"):
                movimientos_restantes += 1
        return movimientos_restantes
my_problem = BusquedaDota(Initial_state)

#v = BaseViewer()
v = WebViewer()
result = astar(my_problem)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")

    print("Final cost:", result.cost)