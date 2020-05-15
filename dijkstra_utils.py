class Node(object):
    def __init__(self, pos, type, distance = float('inf')):
        self.pos = pos
        self.type = type
        self.distance = distance
        self.neighbours = []


    def getPath(self):
        s.path.clear()
        if s.foundFlag == False:
            return
        actualPos = s.pacmanPos
        foundFlag = False
        while foundFlag == False:
            min = float('inf')
            minPos = None
            for delta in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                pos = (actualPos[0] + delta[0], actualPos[1] + delta[1])
                if s.isOnBoard(pos):
                    if s.board[pos[0]][pos[1]] == 'F':
                        foundFlag = True
                        break
                    else:
                        distance = s.algoBoard[pos[0]][pos[1]]
                        if distance > 0 and distance < min:
                            min = distance
                            minPos = pos
            if minPos == None and foundFlag == False:
                print("error, sortie getpath")
                return 84
            if foundFlag == False:
                s.path.append(minPos)
                actualPos = minPos


                    def areNeighbours(self, pos1, pos2):
                        y1, x1 = pos1
                        y2, x2 = pos2
                        if x1 == x2 and (y1 + 1 == y2 or y1 - 1 == y2):
                            return True
                        elif y1 == y2 and (x1 + 1 == x2 or x1 - 1 == x2):
                            return True
                        return False
