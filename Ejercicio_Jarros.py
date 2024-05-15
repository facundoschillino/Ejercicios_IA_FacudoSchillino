#Se tienen N jarros enumerados de 1 a N, donde la capacidad en litros del jarro I es I. 
# Esto es, el jarro 1 tiene capacidad de 1 litro, el jarro 2, 2 litros y así sucesivamente. 
#Inicialmente el jarro N está lleno de agua y los demás están vacíos.
#El objetivo es que todos los jarros queden con 1 litro de agua, teniendo como operaciones 
# permitidas trasvasar el contenido de un jarro a otro, 
# operación que finaliza al llenarse el jarro de destino o vaciarse el jarro de origen.
#Todo esto se tiene que lograr con el menor costo posible, siendo I el costo de 
# trasvasar el contenido del jarro I a otro jarro.
#En este caso concreto se tienen 4 jarros.
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

Goal = (1,1,1,1)
Initial_State = (0,0,0,4)
class ProblemaJarros(SearchProblem):
    def actions(self, state): ##Defino que Jarros voy a trasvasar
        actions = []
        for JarroOrigen, JARcontenido in enumerate(state): #busco el jarro de origen
            if JARcontenido > 1 :    #Si es mayor a uno puede trasvasar
                for JarroDestino, JARROcontenido in enumerate(state): #Busco el jarro de destino
                    if JarroDestino != JarroOrigen: #Verifico que no sea el mismo jarro
                        if JARROcontenido != 1:   #Verifico que el jarro este vacío o que tenga más de uno(No se si darla esta lógica esta bien, creo que puede reventar)
                            if JARROcontenido < JarroDestino + 1: #Verifico que el jarro de destino no este lleno para poder trasvasar
                                actions.append((JarroOrigen,JarroDestino)) #Le doy los jarros a los que tiene que trasvasar
        return actions
    def result (self, state, actions):
        origen, destino = actions
        lo_que_falta_para_llenarse = (destino + 1) - state[destino] #Le resto a la posición mas uno el contenido para sacar el faltante que tiene ese jarro
        #Proximo paso es trasvasar. Tengo que verificar que no se pase del contenido. Lo que puedi hacer es vaciar el jarro y el 
        state = [list(item) for item in state] ## hago esto para convertirlo en una lista y poder trabajarlo
        if (state[origen] > lo_que_falta_para_llenarse):
            state[origen] -= lo_que_falta_para_llenarse
            state[destino] += lo_que_falta_para_llenarse
        else :
            state[destino] += state[origen]
            state[origen] = 0
        state = tuple(tuple(row) for row in state) ## hago esto para volver a convertirlo en una tupla
        return state
    
    def cost(self, state, action, state2):
        return 1
    def heuristic(self, state):
        contador = 0
        for item in state:
            if (item == 0):
                contador += 1
        return contador
    def is_goal(self, state):
        return state == Goal


my_problem = ProblemaJarros(Initial_State)

v = BaseViewer()
result = astar(my_problem)

if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")

    print("Final cost:", result.cost)