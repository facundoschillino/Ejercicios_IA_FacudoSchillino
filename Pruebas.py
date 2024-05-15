def actions(state):
        actions = []
        for JarroOrigen, JARcontenido in enumerate(state): #busco el jarro de origen
            if JARcontenido > 1 :    #Si es mayor a uno puede trasvasar
                for JarroDestino, JARROcontenido in enumerate(state): #Busco el jarro de destino
                    if JarroDestino != JarroOrigen: #Verifico que no sea el mismo jarro
                        if JARROcontenido != 1:   #Verifico que el jarro este vacío o que tenga más de uno(No se si darla esta lógica esta bien, creo que puede reventar)
                            if JARROcontenido < JarroDestino + 1: #Verifico que el jarro de destino no este lleno para poder trasvasar
                                actions.append((JarroOrigen,JarroDestino)) #Le doy los jarros a los que tiene que trasvasar
        return actions

def result (state, actions):
        origen, destino = actions
        lo_que_falta_para_llenarse = (destino + 1) - state[destino] #Le resto a la posición mas uno el contenido para sacar el faltante que tiene ese jarro
        #Proximo paso es trasvasar. Tengo que verificar que no se pase del contenido. Lo que puedi hacer es vaciar el jarro y el 
        if (state[origen] > lo_que_falta_para_llenarse):
            state[origen] -= lo_que_falta_para_llenarse
            state[destino] += lo_que_falta_para_llenarse
        else :
            state[destino] += state[origen]
            state[origen] = 0
        return state


Initial_state = [1,2,0,1]
estado = result(Initial_state, (3,1))


print(estado)
