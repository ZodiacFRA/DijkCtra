import sys

from config import FAILURE


def exit_error(err = None):
    if err is not None:
        print(err, file = sys.stderr)
    sys.exit(FAILURE)


class MapError(Exception):
    pass
