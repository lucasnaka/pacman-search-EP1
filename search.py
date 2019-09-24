# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def aStarSearch(problem, heuristic=nullHeuristic):
    from game import Directions

    # Inicializacao
    initial_state = problem.getStartState()
    initial_path_cost = 0
    initial_objective_cost = heuristic(initial_state,problem)
    priority_state_queue = util.PriorityQueue() # Estados ordenados com relacao ao custo de solucao estimado
    visited_states = [] # Fronteira

    # Adicionamos na lista de prioridades o nosso estado inicial
    priority_state_queue.push((initial_state, [], 0), initial_path_cost + initial_objective_cost)
    # Partimos a busca do estado inicial:
    (state, directions_to_goal, path_cost) = priority_state_queue.pop()
    # Adicionamos o estado inicial a nossa fronteira:
    visited_states.append((state, path_cost + initial_objective_cost))

    while not problem.isGoalState(state): # O problema so para quando um estado solucao e expandido
        successors = problem.getSuccessors(state) # Pegar todos os sucessores de um estado
        # successors contem o seu estado, sua acao (no nosso caso, uma direcao) 
        # e o custo da acao para passar do estado anterior para este estado sucessor
        for (successor_state, successor_action, successor_step_cost) in successors:
            already_expanded = False
            actual_cost = path_cost + successor_step_cost # Custo total do no inicial ate o no atual atraves desse caminho
            for (visitedState,visitedToCost) in visited_states:
                # Se o estado ja se encontra na fronteira com um custo menor do que o custo atual, nao fazer nada
                if (successor_state == visitedState) and (actual_cost >= visitedToCost): 
                    already_expanded = True
                    break

            # Caso contrario, adiciona-lo na fronteira e a lista de prioridade de estados
            if not already_expanded:
                priority_state_queue.push((successor_state,directions_to_goal+[successor_action],actual_cost), actual_cost+heuristic(successor_state,problem)) 
                visited_states.append((successor_state,actual_cost))

        # Reiniciar o looping com o estado de menor custo da fronteira
        (state,directions_to_goal,path_cost) = priority_state_queue.pop()

    return directions_to_goal


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
