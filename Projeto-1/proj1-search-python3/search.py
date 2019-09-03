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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    """util.raiseNotDefined()"""
    #importando a pilha para o algoritmo
    from util import Stack
    #estado atual
    atual = problem.getStartState()
    #lista do possivel caminho, um dicionario composto com as seguintes chaves "Acao", Anterior", "Atual" e se ja foi ou nao percorrido
    possiveisnos = []
    possiveisnos.append({"Acao": None, "Anterior": None, "Atual": atual, "Percorrido": False})

    #Pilha dos estados para realizar o algoritmo de busca em profundidade
    pilha = Stack()
    pilha.push(atual)
    #lista de item explorados
    explorado = []
    #guarda o estado anterior 
    anterior = None
    while not pilha.isEmpty():
        #atualiza o estado
        atual = pilha.pop()
        #verifica se o estado atual eh o final, caso seja ele para o loop
        if problem.isGoalState(atual):
            break
        
        explorado.append(atual)

        for node in possiveisnos:
            if node['Atual'] == atual:
                node["Percorrido"] = True



        #atualiza o no anterior
        anterior = atual

        sucessores = problem.getSuccessors(atual)
        #itera os sucessores e verifica se o mesmo ja foi explorado alguma vez, caso contrario ele adiciona o dicionario na lista de possiveis nos
        for sucessor in sucessores:
            if sucessor[0] not in explorado:
                possiveisnos.append({"Acao": sucessor[1], "Anterior": atual, "Atual": sucessor[0], "Percorrido": False})
                pilha.push(sucessor[0])

        
    
    
    path = []
    #ultimo elemento dos possiveis caminhos (onde esta o ponto)
    elemento = possiveisnos[-1]
    while elemento:
        #chega se o mesmo eh nulo, se for ele so para a iteracao
        if not elemento["Anterior"]:
            break
        #insere no comeco da lista a acao
        path.insert(0, elemento['Acao'])
        #escolhe o procimo caminho a ser escolhido, caso contrario ele eh vazio
        elemento = next((item for item in possiveisnos if item["Atual"] == elemento["Anterior"] and item["Percorrido"] ), None)


    
    print("path: ", path)
    
    return path


    

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
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
