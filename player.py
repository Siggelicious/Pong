from vec2 import Vec2
import settings
import enum

class Actions(enum.Enum):
    UP = enum.auto()
    DOWN = enum.auto()

class Player:
    def __init__(self, pos, size):
        self.score = 0
        self.pos = Vec2(*pos)
        self.vel = 0.0
        self.size = Vec2(*size)
