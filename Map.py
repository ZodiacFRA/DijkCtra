import glob
import random
from misc import MapError


class Map(object):
    """Contains all the map object data, and handles loading etc
    each case contains a bool for isFree (True = empty case) """
    def __init__(s):
        s.file_path = None
        s.width = -1
        s.height = -1
        s.map = None
        s.player_pos = (-1, -1)
        s.enemies_pos = []

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
                    s.enemies_pos.append((y_idx, x_idx))
                elif c == 'P':
                    if s.player_pos != (-1, -1):
                        print("Multiple player locations detected, the last one found will be used")
                    s.player_pos = (y_idx, x_idx)
                elif c != "1":
                    raise MapError(f"{s.file_path}: Invalid character ({c}) on line {y_idx}")
        if not s.enemies_pos or s.player_pos == (-1, -1):
            raise MapError(f"{s.file_path}: Map is missing a player and / or an enemy")
