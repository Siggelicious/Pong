import player
from graphics import Graphics
import settings
from sdl2 import *
from mappings import MAPPINGS
from vec2 import Vec2
import ctypes

class Arena:
    def create_player(self, pos, size):
        self.players.append(player.Player(pos, size))

    def handle_player_input(self, dt):
        kb_state = SDL_GetKeyboardState(None)

        for i in range(len(self.players)):
            direction = 0

            for k, v in MAPPINGS[i].items():
                if kb_state[v]:
                    match k:
                        case player.Actions.UP:
                            direction += 1
                        case player.Actions.DOWN:
                            direction -= 1
            
            self.players[i].vel = direction * settings.PLAYER_VELOCITY

    def render(self, graphics: Graphics):
        graphics.fill_rect((0, 0, *settings.WINDOW_SIZE), (0, 0, 0, 255))
        
        for player in self.players:
            graphics.fill_rect((round(player.pos.x), round(player.pos.y), round(player.size.x), round(player.size.y)), (255, 255, 255, 255))

    def __init__(self, size):
        self.size = Vec2(*size)
        self.players = [] 
        self.create_player(
                (50.0, (settings.ARENA_SIZE[1] - settings.PLAYER_SIZE[1]) / 2),
                (settings.PLAYER_SIZE[0], settings.PLAYER_SIZE[1])
                )
        self.create_player(
                Vec2(settings.ARENA_SIZE[0] - settings.PLAYER_SIZE[0] - 50.0, (settings.ARENA_SIZE[1] - settings.PLAYER_SIZE[1]) / 2.0),
                Vec2(settings.PLAYER_SIZE[0], settings.PLAYER_SIZE[1])
                )
        # TODO: Create ball here!
        entities = []
        entities.extend(self.players)
        # entities.append(ball)
