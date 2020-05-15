from config import *
from Map import Map
from misc import MapError
from pyGameHandler import pyGameHandler


class Core(object):
    def __init__(s, map):
        s.map = map
        s.gI = pyGameHandler(WINDOW_SIZES, s.map.width, s.map.height, MAX_FPS)
        s.gI.set_window_title("pyDijkCtra")

    def run(s):
        while 1:
            inputs = s.gI.update_display(COLOR_BLACK, COLOR_WHITE)
            s.map.move_player(inputs)
