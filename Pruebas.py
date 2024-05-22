INITIAL = ((0,0),((0,0),"rojo"))


def actions(state):
        pos_actual, casillas = state
        actions = []
        posibilidades = [] #Genero las 8 casillas a las que se deberia poder mover
        posibilidades.append((pos_actual[0]+1, pos_actual[1]+2))
        posibilidades.append((pos_actual[0]+2, pos_actual[1]+1))
        posibilidades.append((pos_actual[0]-1, pos_actual[1]+2))
        posibilidades.append((pos_actual[0]+1, pos_actual[1]-2))
        posibilidades.append((pos_actual[0]-1, pos_actual[1]-2))
        posibilidades.append((pos_actual[0]+2, pos_actual[1]-1))
        posibilidades.append((pos_actual[0]-2, pos_actual[1]-1))
        for posibilidad in posibilidades: # Aca voy a suprimir las casillas ya visitadas y las casillas que estan fuera del rango del tablero
            if (posibilidad[0]>=0 and posibilidad[0]<=2 and posibilidad[1] >=0 and posibilidad[1]<=3 and ((posibilidad, "blanco") in casillas)): ## Tengo que verificar en las acciones que el caballo no pueda moverse a una casilla ya visitada?
                actions.append(((posibilidad),"blanco"))
        return  actions
def result(state, action): ##Voy a mover la casilla actual a la de la accion y pintar de rojo
        coord_actual = list(state[0])
        casillas = list(state[1])
        indice = casillas.index(action)
        coord_actual = action

        casillas[indice] = list(casillas[indice])
        casillas[indice][1] = "rojo"
        casillas[indice] = tuple(casillas[indice])
        state = list(state)
        state[0]= tuple(coord_actual)
        state[1] = tuple(casillas)  
        return tuple(state)
ejemplo = ((1, 2), 'blanco')

def is_goal(state):
        goal = True
        for item in state[1]:
            if  "blanco" in item:
                goal = False
        return goal
accion = is_goal(INITIAL)
print(accion)