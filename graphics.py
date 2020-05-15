

    def drawBonuses(self):
        for strPos in s.bonusPoss:
            pos = strPos.split(',')
            s.display.blit(s.icons["bonusIcon"], s.getScreenPosition((int(pos[0]), int(pos[1]))))
