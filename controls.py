
    def handleInput(self):
        pY, pX = s.pacmanPos
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            y = pY - 1
            if y > 0 and s.board[y][pX] == '0':
                s.dir = 0
            else:
                s.wantedDir = 0
        elif keys[K_RIGHT]:
            x = pX + 1
            if x < s.width and s.board[pY][x] == '0':
                s.dir = 1
            else:
                s.wantedDir = 0
        elif keys[K_DOWN]:
            y = pY + 1
            if y < s.heigh and s.board[y][pX] == '0':
                s.dir = 2
            else:
                s.wantedDir = 0
        elif keys[K_LEFT]:
            x = pX - 1
            if x >= 0 and s.board[pY][x] == '0':
                s.dir = 3
            else:
                s.wantedDir = 0
