INITIAL = (3,3)
ENEMIES=((0,0),(0,1),(0,4),(1,4),(2,0),(3,1),(3,6),(0,4),(6,5),(6,3))
def Casillas_atacadas(lista):
    posibilidades = []
    for enemigo in lista:
        fila = enemigo[0]
        columna = enemigo[1]
        posibilidades.append((fila-1, columna))
        posibilidades.append((fila+1,columna))
        posibilidades.append((fila, columna+1))
        posibilidades.append((fila, columna-1))
    return posibilidades
def actions(state):
        actions = []
        bajo_ataque = Casillas_atacadas(ENEMIES)
        fila,columna = state
        posibilidades = []
        posibilidades.append((fila-1, columna))
        posibilidades.append((fila+1,columna))
        posibilidades.append((fila, columna+1))
        posibilidades.append((fila, columna-1))
        for casilla in posibilidades:
            Esta_atacada = False
            Esta_atacada = (casilla in bajo_ataque)
            if (casilla[0] >= 0 and casilla[0] <= 6) and (casilla[1] >= 0 and casilla[1] <= 6) and(Esta_atacada == False):
                actions.append(casilla)
        return actions
acciones = actions(INITIAL)
print (acciones)







