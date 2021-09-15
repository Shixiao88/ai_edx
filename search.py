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
from util import *

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
    
    stack = Stack()
    dic = {}

    for successor in problem.getSuccessors(problem.getStartState()):
        stack.push(successor)
        dic[successor] = problem.getStartState()
    nextState = stack.pop()

    visited = set()
    visited.add(problem.getStartState())
    while (not problem.isGoalState(nextState[0]) or not stack.isEmpty):
        for successor in problem.getSuccessors(nextState[0]):
            if (successor[0] not in visited):
                visited.add(successor[0])
                stack.push(successor)
                dic[successor] = nextState
        nextState = stack.pop()

    step = nextState
    return getTotalActions(step, dic)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    queue = Queue()
    dic = {}
    visited = set()

    for successor in problem.getSuccessors(problem.getStartState()):
        queue.push(successor)
        dic[successor] = problem.getStartState()
        visited.add(successor)
    nextState = queue.pop()
    
    visited.add(problem.getStartState())
    
    while ((not problem.isGoalState(nextState[0])) or (not queue.isEmpty)):
        print("in the while loop", nextState);
        for successor in problem.getSuccessors(nextState[0]):
            if (successor not in visited):
                #print("not in", successor, nextState)
                visited.add(successor)
                queue.push(successor)
                #print("after push", queue.list)
                dic[successor] = nextState
            #print("in visited", successor)
        nextState = queue.pop()

    print(problem.isGoalState(nextState[0]))
    step = nextState
    return getTotalActions(step, dic)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    queue = PriorityQueue()
    dic = {}

    for successor in problem.getSuccessors(problem.getStartState()):
        dic[successor] = problem.getStartState()
        queue.push(successor, problem.getCostOfActions(getTotalActions(successor, dic)))
    nextState = queue.pop()

    visited = set()
    visited.add(problem.getStartState())
    while (not problem.isGoalState(nextState[0]) or not queue.isEmpty):
        for successor in problem.getSuccessors(nextState[0]):
            if (successor[0] not in visited): 
                visited.add(successor[0])
                dic[successor] = nextState
                cost = problem.getCostOfActions(getTotalActions(successor, dic))
                queue.push(successor, cost)
                queue.update(successor, cost)
        nextState = queue.pop()

    step = nextState
    return getTotalActions(step, dic)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    queue = PriorityQueue()
    dic = {}

    for successor in problem.getSuccessors(problem.getStartState()):
        dic[successor] = problem.getStartState()
        queue.push(successor, problem.getCostOfActions(getTotalActions(successor, dic)))
    nextState = queue.pop()

    visited = set()
    visited.add(problem.getStartState())
    while (not problem.isGoalState(nextState[0]) or not queue.isEmpty):
        for successor in problem.getSuccessors(nextState[0]):
            if (successor[0] not in visited): 
                visited.add(successor[0])
                dic[successor] = nextState
                cost = problem.getCostOfActions(getTotalActions(successor, dic)) + heuristic(successor[0], problem)
                queue.push(successor, cost)
                queue.update(successor, cost)
        nextState = queue.pop()

    step = nextState
    return getTotalActions(step, dic)
    
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


def getTotalActions(step, dic):
    moves = Queue()
    while (step in dic):
        moves.push(step[1])
        step = dic[step]
        print(step)
    return moves.list
