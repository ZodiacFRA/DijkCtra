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


    def getScreenPosition(self, pos):
        y = s.base_Y + pos[0] * s.grid_y_inc
        x = s.base_X + pos[1] * s.grid_x_inc
        #INVERTED FOR PYGAME !!!!
        return (x, y)
