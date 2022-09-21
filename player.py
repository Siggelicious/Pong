from vec2 import Vec2
import settings
import enum
from event import Event

class Actions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()

class MovementEvent(Event):
    def __init__(self, player, action, dt):
        self.player = player
        self.action = action
        self.dt = dt

def on_movement_event(event):
    match event.action:
        case Actions.UP:
            event.player.pos.y -= settings.PLAYER_VELOCITY * event.dt

        case Actions.DOWN:
            event.player.pos.y += settings.PLAYER_VELOCITY * event.dt

class Player:
    def __init__(self, pos, size):
        self.score = 0
        self.pos = Vec2(*pos)
        self.size = Vec2(*size)


