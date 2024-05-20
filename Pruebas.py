
INITIAL = ((0,0),((0,0)))
def actions(state):
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
def result (state,action):
        state = list(state)
        Visitadas = state[1]
        state[0] = action
        state[1]= list(state[1])
        state[1].append(action)
        state[1]= tuple(state[1])
        return tuple(state)
resultado = result(INITIAL,(2,1))
print(resultado)
acciones = actions(INITIAL)
print (acciones)