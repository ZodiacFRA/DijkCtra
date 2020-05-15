import sys
import glob
import random

from config import MAPS_PATH


def exit_error(err = None):
    if err is not None:
        print(err, file = sys.stderr)
    sys.exit(ERROR_CODE)


def exit_error_msg(msg):
    print(msg)
    sys.exit(ERROR_CODE)

class MapError(Exception):
    pass
