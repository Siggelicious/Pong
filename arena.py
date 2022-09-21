import player
from graphics import Graphics
import settings
from sdl2 import *
from mappings import MAPPINGS
from event import EventQueue, Event
from vec2 import Vec2
import ctypes

class Arena:
    def create_player(self, pos, size):
        self.players.append(player.Player(pos, size))

    def handle_player_input(self, dt):
        kb_state = SDL_GetKeyboardState(None)

        for i in range(len(self.players)):
            for k, v in MAPPINGS[i].items():
                if kb_state[v]:
                    self.event_queue.push_event(player.MovementEvent(self.players[i], k, dt))

    def register_event(self, event_type, handler):
        self.event_queue.register_event(event_type, handler)

    def handle_events(self):
        self.event_queue.handle_events()

    def render(self, graphics: Graphics):
        graphics.fill_rect((0, 0, *settings.WINDOW_SIZE), (0, 0, 0, 255))
        
        for player in self.players:
            graphics.fill_rect((round(player.pos.x), round(player.pos.y), round(player.size.x), round(player.size.y)), (255, 255, 255, 255))

    def __init__(self, size):
        self.size = Vec2(*size)
        self.players = []
        self.event_queue = EventQueue()
    
