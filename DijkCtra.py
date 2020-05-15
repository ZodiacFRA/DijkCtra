#!/usr/bin/env python3
import random
import time

import pygame
from pygame.locals import *

from config import *
from Map import Map
from misc import MapError



class Core(object):
    def __init__(s, map):
        s.gI = pyGameHandler(WINDOW_HEIGHT, WINDOW_WIDTH, )
        s.gI.set_title("pyDijkCtra")


        s.speed = 0.1

        s.foundFlag = False
        s.path = []

        s.wantedDir = 0
        s.dir = -1

        s.gridIncY = -1
        s.gridIncX = -1
        s.icons = {}

        s.algo = Dijkstra(self)
        s.algoBoard = s.algo.getBoard(s.board)
        s.getPath()
        s.findGridSizes()
        s.initIcons()
        s.updateDisplay()

    def run(self):
        doneTime = time.time()
        moveGhostsFlag = 0
        while 1:
            if time.time() - doneTime > s.speed:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        s.handleInput()
                if s.dir != -1:
                    s.getPath()
                    if moveGhostsFlag > 2:
                        moveGhostsFlag = 0
                        if s.getPath() != 84:
                            s.moveGhosts()
                    s.movePlayer()
                    if s.areNeighbours(s.ghostPos, s.pacmanPos):
                        endFlag = 2
                        break
                    if len(s.bonusPoss) == 0:
                        endFlag = 1
                        break
                    s.algo = Dijkstra(self)
                    s.algoBoard = s.algo.getBoard(s.board)
                    s.updateDisplay()
                    moveGhostsFlag += 1
                doneTime = time.time()
        if endFlag == 2:
            title = pygame.font.Font('./rsc/typos/Pixel.ttf', 40).render("LOST! Try again", False, COLOR_RED)
        else:
            title = pygame.font.Font('./rsc/typos/Pixel.ttf', 40).render("WON! Well done :)", False, COLOR_RED)
        s.display.fill(COLOR_WHITE)
        s.display.blit(title, (WINDOW_WIDTH / 6, WINDOW_HEIGH / 2))
        pygame.display.update()
        time.sleep(3)


if __name__ == '__main__':
    try:
        map = Map().get_random_map(MAPS_PATH)
    except MapError as e:
        print("Map error:', e)
        exit(ERROR)  # TODO: Handle multiple retries etc...
    core = Core(map)
    # core.run()
