    def updateDisplay(self):
        s.display.fill(COLOR_WHITE)
        #s.drawBonuses()
        s.drawAssets()
        s.drawGrid()
        pygame.display.update()

    def drawGrid(self):
        for y in range(s.baseY, WINDOW_HEIGH - s.baseY + 1, s.gridIncY):
            pygame.draw.line(s.display, COLOR_GREY, (s.baseY, y), ((WINDOW_WIDTH - s.baseX), y), 2)
        for x in range(s.baseX, WINDOW_WIDTH - s.baseX + 1, s.gridIncX):
            pygame.draw.line(s.display, COLOR_GREY, (x, s.baseX), (x, (WINDOW_HEIGH - s.baseY)), 2)

    def drawBonuses(self):
        for strPos in s.bonusPoss:
            pos = strPos.split(',')
            s.display.blit(s.icons["bonusIcon"], s.getScreenPosition((int(pos[0]), int(pos[1]))))

    def drawAssets(self):
        for y in range(0, s.heigh):
            for x in range(0, s.width):
                algoC = s.algoBoard[y][x]
                rawC = s.board[y][x]
                if rawC == '1':
                    s.display.blit(s.icons["wallIcon"], s.getScreenPosition((y, x)))
                elif rawC == 'P':
                    s.display.blit(s.icons["pacmanIcon"], s.getScreenPosition(s.pacmanPos))
                elif rawC == 'F':
                    s.display.blit(s.icons["ghostIcon"], s.getScreenPosition(s.ghostPos))
                elif algoC != -1:
                    tmp = "Icon" + str(algoC % 10)
                    tmp2 = "color" + str(algoC // 10)
                    s.display.blit(s.icons[tmp2], s.getScreenPosition((y, x)))
                    s.display.blit(s.icons[tmp], s.getScreenPosition((y, x)))

    def findGridSizes(self):
        s.baseY = int(WINDOW_HEIGH - 0.9 * WINDOW_HEIGH)
        s.baseX = int(WINDOW_WIDTH - 0.9 * WINDOW_WIDTH)
        s.gridIncY = int((WINDOW_HEIGH - 2 * s.baseY) // (s.heigh))
        s.gridIncX = int((WINDOW_WIDTH - 2 * s.baseX) // (s.width))

    def getScreenPosition(self, pos):
        y = s.baseY + pos[0] * s.gridIncY
        x = s.baseX + pos[1] * s.gridIncX
        #INVERTED FOR PYGAME !!!!
        return (x, y)

            def initIcons(self):
                s.icons["pacmanIcon"] = pygame.transform.scale(pygame.image.load("./rsc/icons/pacman.png"), (s.gridIncX, s.gridIncY))
                s.icons["ghostIcon"] = pygame.transform.scale(pygame.image.load("./rsc/icons/ghostV2.png"), (s.gridIncX, s.gridIncY))
                s.icons["wallIcon"] = pygame.transform.scale(pygame.image.load("./rsc/icons/wall.png"), (s.gridIncX, s.gridIncY))
                s.icons["bonusIcon"] = pygame.transform.scale(pygame.image.load("./rsc/icons/bonus.png"), (s.gridIncX, s.gridIncY))
                for i in range(0, 10):
                    tmp = "Icon" + str(i)
                    s.icons[tmp] = pygame.transform.scale(pygame.image.load("./rsc/icons/" + tmp + ".png"), (s.gridIncX, s.gridIncY))
                for i in range(0, 5):
                    tmp = "color" + str(i)
                    s.icons[tmp] = pygame.transform.scale(pygame.image.load("./rsc/icons/" + tmp + ".png"), (s.gridIncX, s.gridIncY))
