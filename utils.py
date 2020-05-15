class Pos(object):
    def __init__(s, y, x):
        s.y = y
        s.x = x

    def __eq__(s, other):
        return s.y == other.y and s.x == other.x

    def __ne__(s, other):
        return not s.__eq__(other)
