from pico2d import load_image, get_time, load_font

import game_world
import game_framework

#새의 크기 : 50*50
#날개짓 속도 : 7

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH=13.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7

class Bird:
    def __init__(self):
        self.x, self.y = 300, 300

        self.frame = 0
        self.frame_h=340
        self.dir = 0
        self.image = load_image('bird_animation.png')

    def update(self):
       pass

    def draw(self):
        if self.dir==0:
            self.image.clip_draw(int(self.frame) * 185, 0, 185, 170, self.x, self.y, 50, 50)
        elif self.dir==1:
            self.image.clip_composite_draw(int(self.frame) * 185, 0, 185, 170, 0, 'h', self.x, self.y, 50, 50)

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if self.frame > 4:
            self.frame_h -= 170
            self.frame = 0

        if self.frame_h == 0 and self.frame > 3:
            self.frame_h = 140
            self.frame = 0