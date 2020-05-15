#!/usr/bin/env python3
"""Algorithm functions"""

from dijkstra_utils import Node

import collections
import copy

class Dijkstra(object):
    """docstring for Dijkstra."""
    def __init__(self, App):
        self.App = App
        self.rootNode = Node(self.App.ghostPos, 'F', 0)
        self.doneNodes = collections.OrderedDict()
        self.notDoneNodes = collections.OrderedDict()
        self.compute()

    def exploreNeighbours(self, actualNode, distance = 0):
        if distance > self.App.width * self.App.heigh:
            return 2
        if self.App.board[actualNode.pos[0]][actualNode.pos[1]] == 'P':
            return 1
        for delta in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            tmpPos = (actualNode.pos[0] + delta[0], actualNode.pos[1] + delta[1])
            if self.App.isOnBoard(tmpPos) and self.App.board[tmpPos[0]][tmpPos[1]] != '1':
                tmpName = str(tmpPos[0]) + ',' + str(tmpPos[1])
                if tmpName not in self.notDoneNodes and tmpName not in self.doneNodes:
                    newNode = Node(tmpPos, self.App.board[tmpPos[0]][tmpPos[1]], distance + 1)
                    self.notDoneNodes[tmpName] = newNode
                else:
                    if tmpName in self.notDoneNodes:
                        newNode = self.notDoneNodes[tmpName]
                    else:
                        newNode = self.doneNodes[tmpName]
                    if distance + 1 < newNode.distance:
                        newNode.distance = distance + 1
                actualNode.neighbours.append(newNode)
        return 0

    def compute(self):
        self.exploreNeighbours(self.rootNode)
        while len(self.notDoneNodes) > 0:
            toDo = self.notDoneNodes.popitem(False)
            flag = self.exploreNeighbours(toDo[1], toDo[1].distance)
            self.doneNodes[toDo[0]] = toDo[1]
            if flag == 1:
                self.App.foundFlag = True
                break
            elif flag == 2:
                self.App.foundFlag = False
                break

    def getBoard(self, board):
        algoBoard = [[-1 for x in range(self.App.width)] for y in range(self.App.heigh)]
        while len(self.doneNodes) > 0:
            name, toDo = self.doneNodes.popitem(False)
            if board[toDo.pos[0]][toDo.pos[1]] == '1':
                raise PacmanError("NODE CREATION ERROR")
            algoBoard[toDo.pos[0]][toDo.pos[1]] = toDo.distance
        return algoBoard
