from pico2d import *
import random


class Ball:
    locate = x, y = 0, 0
    speed = 0
    ball_size = 0

    def __init__(self):
        self.x = random.randint(20,780)
        self.y = 599
        if random.randint(0,1) == 0:
            self.image = load_image('ball21x21.png')
            self.ball_size = 21
        else:
            self.image = load_image('ball41x41.png')
            self.ball_size = 41
        self.speed = random.randint(10,20)

    def fall(self):
        if self.y >= 60+self.ball_size:
            self.y -= self.speed
        else:
            self.y = 60

    def render_ball(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


if __name__ == '__main__':
    running = True
    open_canvas()
    balls = [Ball() for i in range(21)]
    grass = load_image('grass.png')
    delay(10)
    while running:
        clear_canvas()
        grass.draw(400,30)
        for i in balls:
            i.fall()
            print(i.y)
            i.render_ball()

        update_canvas()
        handle_events()
        delay(0.01)
    close_canvas()