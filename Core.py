from config import *
from Map import Map
from pyGameHandler import pyGameHandler
from misc import MapError
from utils import Pos


class Core(object):
    def __init__(s, map):
        s.map = map
        s.gI = pyGameHandler(WINDOW_SIZES, s.map.width, s.map.height, MAX_FPS)
        s.gI.set_window_title("DijkCtra")

    def run(s):
        while 1:
            s.gI.prepare_display(COLOR_WHITE)
            s.gI.draw_grid(COLOR_BLACK)

            for y_idx, y in enumerate(s.map.map):
                for x_idx, _ in enumerate(y):
                    if not s.map.map[y_idx][x_idx]:
                        s.gI.draw("Wall", Pos(y_idx, x_idx))
            s.gI.draw("Player", s.map.player_pos)
            inputs = s.gI.update_display()
            s.map.move_player(inputs)
