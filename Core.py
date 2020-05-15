from config import *
from Map import Map
from pyGameHandler import pyGameHandler
from misc import MapError
from utils import Pos, WALL, PLAYER, ENEMY


class Core(object):
    def __init__(s, map):
        s.map = map
        s.gI = pyGameHandler(WINDOW_SIZES, s.map.width, s.map.height, MAX_FPS)
        s.gI.set_window_title("DijkCtra")

        # s.algo = Dijkstra()

    def run(s):
        while 1:
            s.gI.prepare_display(COLOR_WHITE)
            s.gI.draw_grid(COLOR_BLACK)
            for idx, square in enumerate(s.map.map):
                    if square == WALL:
                        s.gI.draw("Wall", s.map.get_pos(idx))
                    elif square == PLAYER:
                        s.gI.draw("Player", s.map.get_pos(idx))
                    elif square == ENEMY:
                        s.gI.draw("Enemy", s.map.get_pos(idx))
            inputs = s.gI.update_display()

            s.map.move_player(inputs)
            if s.map.player_pos in s.map.enemies_pos:
                print("Lost!")
                exit(SUCCESS)
