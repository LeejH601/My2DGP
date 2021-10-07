from pico2d import *
character = load_image('animation_sheet.png')


filp_flag = 1

if filp_flag == 1 :
    character.clip_composite_draw(frame * 100, 100 * 1 , 100, 100, 0, 'c', x, 90,100,100)
elif filp_flag == -1:
    character.clip_composite_draw(frame * 100, 100 * 1 , 100, 100, 0, 'h', x, 90,100,100)
    