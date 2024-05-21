Base
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

from simpleai.search.viewers import BaseViewer, WebViewer, ConsoleViewer
class BusquedaDota(SearchProblem):
    def actions(self, state):       
        return 
    def result(self, state, action):
        return 
    def cost(self, state, action, state2):
        return 
    def is_goal(self, state):
        return
    def heuristic(self, state):
        return 
my_problem = BusquedaDota(Initial_state)
#v = BaseViewer()
v = WebViewer()
result = astar(my_problem, 1000, viewer=v)
if result is None:
    print("No solution")
else:
    for action, state in result.path():
        print("A:", action)
        print("S:")
        print(*state, sep="\n")
    print("Final cost:", result.cost)