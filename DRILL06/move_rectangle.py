from pico2d import *
import math

open_canvas()

image_grass = load_image('grass.png')
image_char = load_image('character.png')

move_flag_is_rectangle = True
char_direct = 0
char_speed = 20
char_point = [400,90]
radiant = 0
radius = 200
temp_point = [0,0]
frist_point = char_point

while True :
    if(move_flag_is_rectangle == True):
        temp_point = char_point.copy()
        if(char_direct == 0 or char_direct == 4):
            temp_point[0] += char_speed
        elif(char_direct == 1):
            temp_point[1] += char_speed
        elif(char_direct == 2):
            temp_point[0] -= char_speed
        elif(char_direct == 3):
            temp_point[1] -= char_speed
        if(char_direct >= 4):
            if(char_point[0] >= 400.0):
                move_flag_is_rectangle = False
        if(temp_point[0] <= 50 or temp_point[0] >= 750) or (temp_point[1] < 90 or temp_point[1] > 510):    
            char_direct += 1
           
        else:
            char_point = temp_point
        print(char_point)
    else:
        char_point =[
            (math.cos((radiant-90)/180*math.pi) * radius)+ 400,
            (math.sin((radiant-90)/180*math.pi)*radius)+(radius+90)
        ]
        print(radiant)
        print(char_point)
        radiant += 10
        if((radiant-90) >=360):
            move_flag_is_rectangle = True
            radiant = 0
    clear_canvas_now()
    image_grass.draw_now(400,30)
    image_char.draw_now(char_point[0],char_point[1])
    delay(0.02)







delay(5)

close_canvas()
