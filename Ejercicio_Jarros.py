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
Initial_State = [0,0,0,4]



class ProblemaJarros(SearchProblem):
    def actions(self, state):
        actions = []
        for JarroOrigen, JAR in state: #busco el jarro de origen
            if JAR > 1 :    #Si es mayor a uno puede trasvasar
                for JarroDestino, JARRO in state: #Busco el jarro de destino
                    if JarroDestino != numeroJarro: #Verifico que no sea el mismo jarro
                        if JARRO != 1:   #Verifico que el jarro este vacío o que tenga más de uno(No se si darla esta lógica esta bien, creo que puede reventar)
                            if JARRO < JarroDestino + 1: #Verifico que el jarro de destino no este lleno para poder trasvasar
                                actions.append[JarroOrigen,JarroDestino] #Le doy los jarros a los que tiene que trasvasar
        return actions

    def result (self, state, actions):
        origen, destino = actions
        lo_que_falta_para_llenarse = (destino + 1) - state[destino] #Le resto a la posición mas uno el contenido para sacra el faltante que tiene ese jarro
        #Proximo paso es trasvasar. Tengo que verificar que no se pase del contenido. Lo que puedi hacer es vaciar el jarro y el 
        state [destino] = 