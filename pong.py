from graphics import Graphics
import player
from arena import Arena
from sdl2 import *
from vec2 import Vec2
import sys
import ctypes
import settings
import time

def main():
    graphics = Graphics(settings.WINDOW_SIZE)
    running = True
    arena =  Arena(settings.ARENA_SIZE)
    arena.register_event(player.MovementEvent, player.on_movement_event)
    arena.create_player((50.0, (settings.ARENA_SIZE[1] - settings.PLAYER_SIZE[1]) / 2), settings.PLAYER_SIZE)
    arena.create_player((settings.ARENA_SIZE[0] - 50.0 - settings.PLAYER_SIZE[0], (settings.ARENA_SIZE[1] - settings.PLAYER_SIZE[1]) / 2), settings.PLAYER_SIZE)
    event = SDL_Event()
    new_time = old_time = time.process_time_ns()

    while running:
        while SDL_PollEvent(event) != 0:
            if event.type == SDL_QUIT:
                running = False
   
        new_time = time.process_time_ns()
        dt = (new_time - old_time) / 1000000000
        old_time = new_time
        arena.handle_player_input(dt)
        arena.handle_events()
        arena.render(graphics)
        graphics.present()

if __name__ == "__main__":
    sys.exit(main())
