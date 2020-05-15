import glob
import random

from misc import MapError
from utils import Pos


class Map(object):
    """Contains all the map object data, and handles loading etc
    each case contains a bool for isFree (True = empty case) """
    def __init__(s):
        s.file_path = None
        s.width = -1
        s.height = -1
        s.map = None
        s.player_pos = None
        s.enemies_pos = []

    def move_player(s, inputs):
        old_player_pos = s.player_pos
        if inputs == 0:
            y = s.player_pos.y - 1
            if y > 0 and s.map[y][s.player_pos.x]:
                s.player_pos.y = y
        elif inputs == 1:
            x = s.player_pos.x + 1
            if x < s.width and s.map[s.player_pos.y][x]:
                s.player_pos.x = x
        elif inputs == 2:
            y = s.player_pos.y + 1
            if y < s.height and s.map[y][s.player_pos.x]:
                s.player_pos.y = y
        elif inputs == 3:
            x = s.player_pos.x - 1
            if x >= 0 and s.map[s.player_pos.y][x]:
                s.player_pos.x = x
        s.map[old_player_pos.y][old_player_pos.x] = True


    def get_random_map(s, maps_folder_path):
        """Get a random map file data from those available in the folder,
        perform basic error checks and then parse it"""

        maps = glob.glob(maps_folder_path + "*.map")
        if not maps: raise MapError(f"{maps_folder_path}: No map files found")
        s.file_path = random.choice(maps)
        with open(s.file_path) as f:
            map_raw = f.read()
        map_raw = [l.strip() for l in map_raw.split('\n') if l.strip()]
        if not map_raw: raise MapError(f"{s.file_path}: Empty map file")
        s.parse_map(map_raw)

    def parse_map(s, map_raw):
        s.width = len(map_raw[0])
        s.height = len(map_raw)
        if s.width < 2 or s.height < 2:
            raise MapError(f"{s.file_path}: Map too small ({s.width} x {s.height})")
        s.map = [[True for x in range(s.width)] for y in range(s.height)]

        for y_idx, l in enumerate(map_raw):
            if len(l) != s.width:
                raise MapError(f"{s.file_path}: Invalid length {len(l)} for line {y_idx}")
            for x_idx, c in enumerate(l):
                if c == '0':
                    s.map[y_idx][x_idx] = False
                elif c == 'E':
                    s.enemies_pos.append(Pos(y_idx, x_idx))
                elif c == 'P':
                    if s.player_pos:
                        print("Multiple player locations detected, the last one found will be used")
                    s.player_pos = Pos(y_idx, x_idx)
                elif c != "1":
                    raise MapError(f"{s.file_path}: Invalid character ({c}) on line {y_idx}")
        if not s.enemies_pos or not s.player_pos:
            raise MapError(f"{s.file_path}: Map is missing a player and / or an enemy")
