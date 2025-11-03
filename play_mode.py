from pico2d import *

from boy import Boy
from bird import Bird
from grass import Grass
import game_world

import game_framework


boy = None

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global bird
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    bird = Bird()
    birds_xy=[(200, 450), (400, 500), (600, 420),
    (800, 480), (1000, 460), (1200, 430),
    (1400, 490), (300, 440), (1100, 520),(500, 470)]

    for b in birds_xy:
        bird = Bird()
        bird.x, bird.y = b
        game_world.add_object(bird, 2)

def update():
    game_world.update()
    # delay(0.1)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

