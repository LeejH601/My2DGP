import game_framework
from pico2d import *
from ball import Ball

import game_world
from random import randint

# 기본적으로 새의 종류를 참새라 가정하고 그에 맞게 크기와 속도를 책정했다.
# 참새의 이동속도는 평균적으로 29~40km 이다. 고로 이 그 평균값은 35km를 새의 이동속도로 정했다.
# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_RUN_SPEED_KMPH = 35.0  # Km / Hour
BIRD_RUN_SPEED_MPM = (BIRD_RUN_SPEED_KMPH * 1000.0 / 60.0)
BIRD_RUN_SPEED_MPS = (BIRD_RUN_SPEED_MPM / 60.0)
BIRD_RUN_SPEED_PPS = (BIRD_RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed


class BirdRunState:
    
    TIME_PER_ACTION = 0.7
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 14

    def enter(bird, event):
        if randint(0,1) == 0:
            bird.velocity += BIRD_RUN_SPEED_PPS
        else:
            bird.velocity -= BIRD_RUN_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        bird.velocity = 0
        pass

    def do(bird):
        #boy.frame = (boy.frame + 1) % 8
        bird.frame = (bird.frame + BirdRunState.FRAMES_PER_ACTION * BirdRunState.ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if bird.x == 25 or bird.x == 1600 - 25:
            bird.velocity = -bird.velocity


    def draw(bird):
        print(int(bird.frame))
        if bird.velocity > 0:
            bird.image.clip_composite_draw( int(bird.frame) * 100 , 0, 100, 100, 0, ' ', bird.x, bird.y, bird.size_x, bird.size_y)
            # bird.image.clip_draw(int(bird.frame) * 100, 100, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_composite_draw( int(bird.frame) * 100 , 0, 100, 100, 0, 'h', bird.x, bird.y, bird.size_x, bird.size_y)
            # bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class Bird:

    image = None

    def __init__(self):
        self.x, self.y = randint(100, 1500), 400
        self.size_x, self.size_y = 22, 22
        # 일반적으로 참새의 크기는 10~20cm 로 알려져 있다. 사람의 키가 180cm이므로 참새의 크기는 사람의 9분의 1의 크기를 가진다고 가정했다.
        # 그리고 사람의 픽셀크기는 100이므로 그의 9분의 1은 약 11이 된다.
        # 그러나, 크기 11은 화면상에서 너무 작았기 때문에 그 2배인 22를 책정하였다.
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = BirdRunState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return 0, 0, 0, 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))


