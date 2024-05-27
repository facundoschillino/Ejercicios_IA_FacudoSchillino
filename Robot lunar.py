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
Initial_state = ((100),(0,1),((2,0),(3,1),(0,2),(0,3)),0) #Batería, robot, muestras restantes, cantidad de muestras recogidas
Base = (0,1)



from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer
class RobotLunarBusqueda(SearchProblem):
    def actions(self, state):
        bateria, posicion_robot, muestras, muestras_recogidas = state
        fila_robot, columna_robot = posicion_robot
        actions = []
        movimientos = []
        movimientos.append((fila_robot +1, columna_robot))
        movimientos.append((fila_robot -1, columna_robot))
        movimientos.append((fila_robot , columna_robot+1))
        movimientos.append((fila_robot , columna_robot-1))
        for posible_movimiento in movimientos :
            if (posible_movimiento[1] >=0 and posible_movimiento[0] >=0 and posible_movimiento[1] <= 3 and posible_movimiento[0] <=3 and bateria> 10): #Verifico que no se salga de las coordenadas y que tenga bateria
                actions.append(("moverse",(posible_movimiento)))
        if (posicion_robot in muestras and bateria > 25):
            actions.append(("muestrear", posicion_robot)) #Si esta sobre una muestra y tiene bateria puede recogerla
        if (posicion_robot == Base):
            if (bateria >5 and muestras_recogidas > 0):
                actions.append(("dejar muestra", posicion_robot)) #Si tengo bateria puedo dejar
            actions.append(("cargar", posicion_robot)) #Siempre que este en la base puede cargar la bateria
        return actions
    
    def result(self, state, action):
        accion, posicion = action
        state = list(state)
        bateria, posicion_robot, muestras, muestras_recogidas = state
        posicion_robot = list(posicion_robot)
        muestras = list(muestras)
        if accion == "moverse":
            posicion_robot = posicion
            state[1] = tuple(posicion_robot)
            state[0] -= 10
        elif accion == "muestrear":
            state[3] += 1
            state[0] -= 25
            muestras.remove(posicion)
            state[2] = tuple(muestras)
        elif accion == "dejar muestra":
            state[3] -= 1
            state[0] -= 5
        else:
            state[0] = 100
        return tuple(state)
    def cost(self, state, action, state2):
        accion, _ = action
        if accion == "moverse":
            return 5
        elif accion == "muestrear":
            return 15
        elif accion == "dejar muestra":
            return 5
        else: return 0  
    def is_goal(self, state):
        _,_,restantes,muestras = state
        cuanto_falta = len(restantes)
        return (cuanto_falta == 0 and  muestras == 0)
    def heuristic(self, state): ## La heuristica es la cantidad de muestras que le falta tomar
        return (len(state[2] * 15))
my_problem = RobotLunarBusqueda(Initial_state)
v = BaseViewer()
#v = WebViewer()
result = astar(my_problem, 1000, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)