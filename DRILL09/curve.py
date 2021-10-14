import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1920, 1080)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 1):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 1):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 1):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)

def get_next_f_points():
    global cur_index
    start = cur_index % num_points
    # cur_index와 num_points 간의 나머지 연산을 하였기 때문에 인덱스에서 벗어나는 일 없이 루프할 수 있음.

    end = start + 4
    points = extend_point_list[start:end]
    cur_index += 1
    return points


prepare_turtle_canvas()

p1 = (100, 100); p2 = (-50, 400); p3 = (-200, -200); p4 = (400, -50)

draw_big_point(p1)
draw_big_point(p2)
draw_big_point(p3)
draw_big_point(p4)

cur_index = -1 # -1로 시작하는 이유는 맨 처음 시작이 p1이 되도록 하기 위함
point_list = [p1,p2,p3,p4] # 편의를 위하여 점들을 리스트로 저장
num_points = len(point_list)
extend_point_list = point_list + point_list[:3]

t = 0
P1, P2, P3, P4 = get_next_f_points()

turtle.goto(-400,400)
turtle.write('2018182031 이지형')

draw_curve_4_points(p1,p2,p3,p4)


while True:
    # 4점 곡선 그리기에서 중간 2~3점 사이를 그리는 공식
    cx = ((-t**3 + 2*t**2 - t)*P1[0] + (3*t**3 - 5*t**2 + 2)*P2[0] + (-3*t**3 + 4*t**2 + t)*P3[0] + (t**3 - t**2)*P4[0])/2
    cy = ((-t**3 + 2*t**2 - t)*P1[1] + (3*t**3 - 5*t**2 + 2)*P2[1] + (-3*t**3 + 4*t**2 + t)*P3[1] + (t**3 - t**2)*P4[1])/2

    t += 0.02 # t를 2% 씩 증가 시킨다.
    if t >= 1.0:
        P1, P2, P3, P4 = get_next_f_points()
        t = 0

    draw_point((cx,cy))


turtle.done()