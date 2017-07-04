NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.advance_map = {NORTH: (0, 1),
                            EAST: (1, 0),
                            SOUTH: (0, -1),
                            WEST: (-1, 0)
                            }
        self.command_map = {'A': self.advance,
                            'R': self.turn_right,
                            'L': self.turn_left
                            }

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        self.x += self.advance_map[self.bearing][0]
        self.y += self.advance_map[self.bearing][1]
        self.coordinates = (self.x, self.y)

    def simulate(self, instr):
        for step in instr:
            self.command_map[step]()
