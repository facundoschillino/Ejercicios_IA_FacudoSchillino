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

Dimension_tablero = (3,4)
Obstaculos = ((0,2),(2,1),(1,3))
initial_state = ((0,1),(0,1))
GOAL = ((3,2)(0,4))

class Robots_Defensivos(SearchProblem):

    def actions(self, state):
        actions = [[],[]]
        for cual_es, robot in enumerate(state):
            
