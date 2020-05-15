#!/usr/bin/env python3
from misc import MapError
from Map import Map
from Core import Core
from config import *


def main():
    map = Map()
    try:
        map.get_random_map(MAPS_PATH)
    except MapError as e:
        print("Map error:", e)
        exit(FAILURE)  # TODO: Handle multiple map loading retries etc...
    core = Core(map)
    core.run()


if __name__ == '__main__':
    main()
