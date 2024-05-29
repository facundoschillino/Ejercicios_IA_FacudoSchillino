

import itertools
INCIAL = (("CAP","CAP","COM","COM","CEN","CEN"),(),())
#GOAL = ((),(),(CAP,CAP,COM,COM,CEN,CEN))

def is_goal(self, state):
    return state == GOAL

def actions(self,state):
    hab1,hab2,hab3 = state
    actions = []
    
    for indice,hab in enumerate(state):
        combinaciones_con_iguales = itertools.combinations(hab,2)
        combinaciones_con_iguales = set (combinaciones_con_iguales)
        
        if hab != () and indice != 2: #No me sirve recorrer la tercer habitacion porque de ahi no muevo nada
            set_sin_iguales = set(hab) #Con esto elimino la posibilidad de pasar 2 iguales a una habitación
            for indicepresidente,presidente in enumerteh(hab): #aca recorro la habitacion para ver a cada presidente
                combinaciones = itertools.combinations(set_hab) # Esto me da las posibles combinaciones para pasar de a 2
                if (hab[indice+1] != presidente): ##No hay un presidente del mismo tipo en la otra habitacion
                    actions.append((presidente,indice+1)) #Appendeo la posibilidad de traspasar un solo presidente  a la habitacion contigua




            for combs in set_con_iguales:#aca recorro las combinaciones CON LOS IGUALES (CAP,CAP) POR EJEMPLO
                pres1,pres2 = combs #descuajeringamos
                if (pres1 != pres2 and pres1 not in state[indice-1] and pres2 not in state[indice-1]): #Con esto verifico que los presidentes (que son de distitnto tipo (CAP,COM) no esten mas de una habitacion distantes
                    actions.append((combs),indice+1)
                if (pres1 == pres2 and hab[indice+1] != ()): #Si la habitacion no esta vacia puedo mover 2 iguales
                                    


combinaciones = itertools.combinations(INCIAL[0],2)
combinaciones = set(combinaciones)
print (combinaciones)
