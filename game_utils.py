
    def moveGhosts(self):
        if len(s.path) < 1:
            return
        newPos = s.path[-1]
        s.board[s.ghostPos[0]][s.ghostPos[1]] = '0'
        s.ghostPos = newPos
        s.board[newPos[0]][newPos[1]] = 'F'

    def movePlayer(self):
        pY, pX = s.pacmanPos

        if s.dir == 0:
            y = pY - 1
            if y > 0 and s.board[y][pX] == '0':
                pY = y
        elif s.dir == 1:
            x = pX + 1
            if x < s.width and s.board[pY][x] == '0':
                pX = x
        elif s.dir == 2:
            y = pY + 1
            if y < s.heigh and s.board[y][pX] == '0':
                pY = y
        elif s.dir == 3:
            x = pX - 1
            if x >= 0 and s.board[pY][x] == '0':
                pX = x
        s.board[s.pacmanPos[0]][s.pacmanPos[1]] = '0'
        s.pacmanPos = (pY, pX)
        s.board[pY][pX] = 'P'
        if (str(pY) + ',' + str(pX)) in s.bonusPoss:
            s.bonusPoss.remove(str(pY) + ',' + str(pX))

    def isOnBoard(self, pos):
        return pos[0] >= 0 and pos[0] < s.heigh and pos[1] >= 0 and pos[1] < s.width

    def getFreePos(self):
        y, x = 0, 0
        while s.board[y][x] != '0':
            y = random.randint(1, s.heigh - 2)
            x = random.randint(1, s.width - 2)
        return y, x

    def isAreaFree(self, y, x):
        return (s.board[y - 1][x - 1] == '0' and
                s.board[y - 1][x] == '0' and
                s.board[y - 1][x + 1] == '0' and
                s.board[y][x - 1] == '0' and
                s.board[y][x] == '0' and
                s.board[y][x + 1] == '0' and
                s.board[y + 1][x - 1] == '0' and
                s.board[y + 1][x] == '0' and
                s.board[y + 1][x + 1] == '0')
