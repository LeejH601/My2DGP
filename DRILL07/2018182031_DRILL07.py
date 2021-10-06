from pico2d import *
import threading
import math
from random import randint

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
goal_place_x, goal_place_y = 0,0
ch_state = 0
ch_point_x, ch_point_y = 400,300
ch_foward_Vecter_x,ch_foward_Vecter_y = (1,0)
rand_cnt = 0

def handle_events():
    global running
    global dir
    global filp_flag
    global ch_state,ch_point_y,ch_point_x,ch_foward_Vecter_x,ch_foward_Vecter_y
    events = get_events()
                

def make_hand():
    global goal_place_x, goal_place_y, rand_cnt
    rand_cnt += 1
    goal_place_x, goal_place_y = randint(30,KPU_WIDTH-30), randint(30, KPU_HEIGHT-30)
    set_forward()

def set_forward():
    global ch_state,ch_point_y,ch_point_x,ch_foward_Vecter_x,ch_foward_Vecter_y
    size_of_vector = math.sqrt((goal_place_x-ch_point_x)**2+(goal_place_y-ch_point_y)**2)
    print(goal_place_x)
    print(goal_place_y)
    ch_foward_Vecter_x = (goal_place_x-ch_point_x)/size_of_vector
    ch_foward_Vecter_y = (goal_place_y-ch_point_y)/size_of_vector
    ch_state = 1


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


running = True
x = 800 // 2
frame = 0
dir = 0 # -1 left, +1 right
filp_flag = 1
speed = 1

make_hand()
rand_cnt = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    hand.clip_draw(0,0,50,52,goal_place_x,goal_place_y)
    if ch_foward_Vecter_x > 0 :
        character.clip_composite_draw(frame * 100, 100 * 1 , 100, 100, 0, 'c', ch_point_x, ch_point_y,100,100)
    elif ch_foward_Vecter_x < 0:
        character.clip_composite_draw(frame * 100, 100 * 1 , 100, 100, 0, 'h', ch_point_x, ch_point_y,100,100)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if ch_state == 1:
        ch_point_x = ch_point_x + ch_foward_Vecter_x*speed
        ch_point_y = ch_point_y + ch_foward_Vecter_y*speed
        if goal_place_x - ch_point_x <= 1 and goal_place_y - ch_point_y <=1:
            ch_state = 0
            make_hand()
            print(rand_cnt)
            if rand_cnt > 1:
                print('오류')
            rand_cnt = 0
    delay(0.01)

close_canvas()

