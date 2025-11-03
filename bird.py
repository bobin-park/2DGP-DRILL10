from pico2d import *

class Bird:
    def __init__(self):
        self.x, self.y = 400, 90

        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 200, 0, 100, 175, self.x, self.y)
