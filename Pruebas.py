from simpleai.search import (
    SearchProblem,
    astar,
)
Initial_state = (100, (0, 1), ((2, 0), (3, 1), (0, 2), (0, 3)), 0)  # Batería, robot, muestras restantes, cantidad de muestras recogidas
Base = (0, 1)

from simpleai.search.viewers import BaseViewer

class RobotLunarBusqueda(SearchProblem):
    def actions(self, state):
        bateria, posicion_robot, muestras, muestras_recogidas = state
        fila_robot, columna_robot = posicion_robot
        actions = []
        movimientos = []
        movimientos.append((fila_robot + 1, columna_robot))
        movimientos.append((fila_robot - 1, columna_robot))
        movimientos.append((fila_robot, columna_robot + 1))
        movimientos.append((fila_robot, columna_robot - 1))
        
        for posible_movimiento in movimientos:
            if 0 <= posible_movimiento[0] <= 3 and 0 <= posible_movimiento[1] <= 3 and bateria > 10:
                actions.append(("moverse", posible_movimiento))
                
        if posicion_robot in muestras and bateria > 25:
            actions.append(("muestrear", posicion_robot))
            
        if posicion_robot == Base:
            if bateria > 5 and muestras_recogidas > 0:
                actions.append(("dejar muestra", posicion_robot))
            actions.append(("cargar", posicion_robot))
            
        return actions

    def result(self, state, action):
        accion, posicion = action
        bateria, posicion_robot, muestras, muestras_recogidas = state
        posicion_robot = list(posicion_robot)
        muestras = list(muestras)
        
        if accion == "moverse":
            posicion_robot = posicion
            bateria -= 10
        elif accion == "muestrear":
            muestras_recogidas += 1
            bateria -= 25
            muestras.remove(posicion)
        elif accion == "dejar muestra":
            muestras_recogidas -= 1
            bateria -= 5
        elif accion == "cargar":
            bateria = 100
        
        return bateria, tuple(posicion_robot), tuple(muestras), muestras_recogidas

    def cost(self, state, action, state2):
        accion, _ = action
        if accion == "moverse":
            return 5
        elif accion == "muestrear":
            return 15
        elif accion == "dejar muestra":
            return 10
        elif accion == "cargar":
            return 30
        return 0

    def is_goal(self, state):
        _, _, muestras_restantes, muestras_recogidas = state
        return len(muestras_restantes) == 0 and muestras_recogidas == 0

    def heuristic(self, state):
        muestras_restantes = len(state[2])
        return muestras_restantes * 15  # Asumimos que cada muestra toma 15 minutos

my_problem = RobotLunarBusqueda(Initial_state)
v = BaseViewer()
result = astar(my_problem, viewer=v)

if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)
