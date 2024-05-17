GOAL = ((3,5),3, []) ##Posicion a la que tiene que llegar, cantidad de comidas que tiene que adquirir, posicion de las comidas
Initial_state = ((3,5), 0, [(1,2),(3,4),(4,0)]) ##Me conviene mas pensarlo como un diccionario donde tengo : Posicion, cantidades comidas, y comidas restantes.
Obstaculos = ((0,3),(0,5),(1,3),(1,1),(2,2),(2,4),(3,0),(4,1),(4,3),(4,5),(5,3))
def result(state, actions):
        origen, destino = actions
        Comidas = state[2]
        estado = list(state)
        for pos,comida in enumerate(Comidas): ##Si hay una comida, la come
            es_comida = (comida == destino)
            if es_comida:
                state[2].remove(comida)
                estado[1] +=1 
        estado [0] = destino
        estado = tuple(estado)
        return estado
    
resultados = result(Initial_state, ((3,5),(3,4)))
print (resultados)



