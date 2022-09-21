from sdl2 import *
import player

MAPPINGS = {
    0 : {
        player.Actions.UP : SDL_SCANCODE_W,
        player.Actions.DOWN : SDL_SCANCODE_S
    },
    1 : {
        player.Actions.UP : SDL_SCANCODE_I,
        player.Actions.DOWN : SDL_SCANCODE_K
    } 
}
